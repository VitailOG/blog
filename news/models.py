from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(verbose_name='Заголовок питаня', max_length=150)
    image = models.ImageField(verbose_name='Картинка питання', upload_to='image_news/', null=True, blank=True)
    text = models.TextField(verbose_name='Текст питання')
    view = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новинa'
        verbose_name_plural = 'Новини'

    def get_not_parent_comment(self):
        return self.comment_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse('detail_news', kwargs={'pk': self.id})


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото профілів', upload_to='image_user/')

    def __str__(self):
        return f"Фото - {self.user.username}"

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.user.id})

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографії'
        ordering = ['-id']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст коментаря")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    like = models.ManyToManyField(User, related_name='users')

    def get_count_like(self):
        return self.like.count()

    def get_absolute_url(self):
        return reverse('detail_news', kwargs={'pk': self.news.id})

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
