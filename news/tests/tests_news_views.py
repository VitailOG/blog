from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, RequestFactory, Client
from ..views import *
from ..models import *


User = get_user_model()


class TestViewNews(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create(username="user1", password="Q2d$a6#3ve5w3")
        self.news = News.objects.create(author=self.user,
                                        title='Title',
                                        image=SimpleUploadedFile(name='test_image.jpg', content=b'',
                                                                 content_type='image/jpeg'),
                                        text='Full test news',
                                        view=100,
                                        date='2018-02-01'
                                        )

        self.request = self.factory.get('')
        self.request.user = self.user

    def test_show_news_page_for_autenticated_user(self):
        response = ShowNewsView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)

    def test_show_news_page_for_not_autenticated_user(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)

    def test_show_detail_news_page_for_autenticated_user(self):
        response = NewsDetailView.as_view()(self.request, pk=f'{self.news.id}')
        self.assertEqual(response.status_code, 200)

    def test_show_detail_news_page_for_not_autenticated_user(self):
        response = self.client.get(f'/update/{self.news.id}')
        self.assertEqual(response.status_code, 302)

    def test_profile_page_user(self):
        response = ProfileDetailView.as_view()(self.request, pk=f'{self.user.id}')
        self.assertEqual(response.status_code, 200)

    def test_users_page(self):
        response = UsersView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_posts_users(self):
        response = ArticleUserView.as_view()(self.request, pk=f'{self.user.id}')
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        response = NewsDeleteView.as_view()(self.request, pk=f'{self.news.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        response = NewsUpdateView.as_view()(self.request, pk=f'{self.news.id}')
        self.assertEqual(response.status_code, 200)

    def test_image_user(self):
        response = self.client.post('/img-user')
        self.assertEqual(response.status_code, 302)

    def test_add_post(self):
        request = self.factory.post('', {
            'title': 'any title',
            'image': self.news.image,
            'text': 'any text'
        })
        request.user = self.user
        response = AddNewsView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_add_comment(self):
        form = CommentFrom({
            'user': self.user,
            'text': 'twerewr',
            'news': self.news
        })
        request = self.factory.post('')
        request.user = self.user
        response = CommentView.as_view()(request, pk=f'{self.news.id}')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(form.is_valid())
