# Generated by Django 2.2.2 on 2019-08-25 05:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20190823_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, related_name='post_bookmarks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
    ]
