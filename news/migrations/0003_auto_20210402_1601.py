# Generated by Django 3.1.7 on 2021-04-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210401_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_news/', verbose_name='Картинка питання'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(verbose_name='Текст питання'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок питаня'),
        ),
    ]