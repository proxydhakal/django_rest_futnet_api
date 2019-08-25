from django.db import models
from apis.venue_detail.models import VenueList
# Create your models here.

class Offer(models.Model):
    title = models.CharField(max_length=255,null= True)
    detail = models.TextField()
    cover_image=models.ImageField(upload_to='medial/offers')
    venue =models.ForeignKey(VenueList,on_delete=models.SET_NULL,null=True)


class Event(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    cover_image= models.ImageField(upload_to='medial/events')
    date_time= models.DateTimeField()
    location = models.CharField(max_length=255)