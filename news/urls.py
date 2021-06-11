from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowNewsView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='detail_news'),
    path('update/<int:pk>', NewsUpdateView.as_view(), name='update_news'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='delete'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('add-news', AddNewsView.as_view(), name='add_news'),
    path('img-user', ImageUserView.as_view(), name='image_user'),
    path('comment/<int:pk>', CommentView.as_view(), name='comment'),
    path('users', UsersView.as_view(), name='users'),
    path('article/<int:pk>/', ArticleUserView.as_view(), name='art'),
    path('like/', LikeView.as_view(), name='like'),

    path('logout', UserLogout.as_view(), name='logout')
]
