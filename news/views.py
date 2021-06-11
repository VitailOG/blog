from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.core.paginator import Paginator, EmptyPage
from django.db.models import F
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from .forms import CommentFrom
from .models import News, UserImage, Comment


class LoginRequired(LoginRequiredMixin):
    login_url = reverse_lazy('account_login')


class ShowNewsView(LoginRequired, ListView):
    """Показ статей"""
    model = News
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = self.page_pagination(News.objects.all().select_related('author')
                                               .prefetch_related('author__userimage_set')[::-1])
        return context

    def page_pagination(self, qs):
        """Пагінація"""
        element = Paginator(qs, 3)
        page_num = self.request.GET.get('page', 1)
        try:
            page = element.page(page_num)
        except EmptyPage:
            page = element.page(1)
        return page


class NewsDetailView(LoginRequired, DetailView):
    """Окремі статті"""
    model = News
    queryset = News.objects.select_related('author').prefetch_related('author__comment_set__comment_set')
    template_name = 'news/detail_news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.model.objects.filter(pk=self.kwargs.get('pk')).update(view=F('view')+1)
        return context


class AddNewsView(LoginRequired, CreateView):
    """Створення новин"""
    model = News
    fields = ['title', 'image', 'text']
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.instance.date)
        return super().form_valid(form)


class ImageUserView(LoginRequired, CreateView):
    model = UserImage
    fields = ['image']
    template_name = 'news/img.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommentView(View):
    def post(self, request, pk, *args, **kwargs):
        news = News.objects.filter(id=pk).first()
        comment = CommentFrom(request.POST or None)
        if comment.is_valid():
            form = comment.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.user = self.request.user
            form.news = news
            form.save()
        return redirect(news.get_absolute_url())


class NewsUpdateView(LoginRequired, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'news/update_news.html'
    fields = ['title', 'image', 'text']
    success_url = reverse_lazy('news')

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class NewsDeleteView(LoginRequired, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'news/detail_news.html'
    success_url = reverse_lazy('news')

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


class ProfileDetailView(LoginRequired, DetailView):
    """Профіль користувача"""
    model = User
    queryset = User.objects.prefetch_related('userimage_set')
    template_name = 'news/profile.html'
    context_object_name = 'profile'


class UsersView(LoginRequired, View):
    """Всі користувачі"""
    def get(self, request, *args, **kwargs):
        context = {
            'user': User.objects.all().prefetch_related('userimage_set', 'author', 'comment_set').order_by('username')
        }
        return render(request, 'news/users.html', context)


class ArticleUserView(LoginRequired, View):
    """Окремі статті користувачів"""
    def get(self, request, *args, **kwargs):
        user = News.objects.filter(author_id=kwargs.get('pk')).prefetch_related('author__userimage_set')
        context = {
            'user': user,
            'username': User.objects.filter(id=kwargs.get('pk')).first()
        }
        return render(request, 'news/other.html', context)


class LikeView(View):
    """Лайки"""
    def post(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=request.POST.get("id_comment"))
        if comment.like.filter(id=request.user.id).exists():
            comment.like.remove(request.user)
        else:
            comment.like.add(request.user)
        return redirect(comment.get_absolute_url())


class UserLogout(LogoutView):
    """клас для кнопки виходу з профіля"""
    next_page = reverse_lazy('account_login')
