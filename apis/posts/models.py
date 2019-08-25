from django.db import models
from django.conf import settings
from django.urls import reverse
from apis.venue_detail.models import VenueList
# Create your models here.



class Post(models.Model):
    CHOICES =(("0","Morning(6am to 9am)"),("1","Day(9am to 4pm)"),("2","Evening(4pm to 7pm)"))
    time =models.CharField(choices=CHOICES, max_length=2)
    date = models.DateField()
    venue =models.ForeignKey(VenueList,on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,related_name='posts')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"pk": self.pk})

    def get_api_like_url(self):
        return reverse("like-api-toggle", kwargs={"pk": self.pk})

class Feedback(models.Model):
    commentator=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,related_name='commented_by')
    post = models.ForeignKey(Post, on_delete=models.CASCADE ,related_name='comments')
    comment =models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Bookmark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE ,related_name='bookmark_posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True,related_name='added_by')
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return self.post