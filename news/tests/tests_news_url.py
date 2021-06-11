from django.test import TestCase
from django.urls import reverse, resolve
from ..views import *


class TestUrlNews(TestCase):

    def setUp(self) -> None:
        self.home_page = reverse('news')
        self.detail_news_page = reverse('detail_news', args=[1])
        self.update_news = reverse('update_news', args=[1])
        self.delete_news = reverse('delete', args=[1])
        self.profile_page = reverse('profile', args=[1])
        self.add_news = reverse('add_news')
        self.image_user = reverse('image_user')
        self.comment = reverse('comment', args=[1])
        self.users = reverse('users')
        self.article_user_page = reverse('art', args=[1])
        self.like = reverse('like')

    def test_home_page(self):
        self.assertEqual(resolve(self.home_page).func.view_class, ShowNewsView)

    def test_detail_news_page(self):
        self.assertEqual(resolve(self.detail_news_page).func.view_class, NewsDetailView)

    def test_update_news(self):
        self.assertEqual(resolve(self.update_news).func.view_class, NewsUpdateView)

    def test_delete_news(self):
        self.assertEqual(resolve(self.delete_news).func.view_class, NewsDeleteView)

    def test_profile_page(self):
        self.assertEqual(resolve(self.profile_page).func.view_class, ProfileDetailView)

    def test_add_news(self):
        self.assertEqual(resolve(self.add_news).func.view_class, AddNewsView)

    def test_image_user(self):
        self.assertEqual(resolve(self.image_user).func.view_class, ImageUserView)

    def test_comment(self):
        self.assertEqual(resolve(self.comment).func.view_class, CommentView)

    def test_users(self):
        self.assertEqual(resolve(self.users).func.view_class, UsersView)

    def test_article_user_page(self):
        self.assertEqual(resolve(self.article_user_page).func.view_class, ArticleUserView)

    def test_like(self):
        self.assertEqual(resolve(self.like).func.view_class, LikeView)


