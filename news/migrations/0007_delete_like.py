# Generated by Django 3.1.7 on 2021-04-04 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
