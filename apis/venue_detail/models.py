from django.db import models

# Create your models here.
class VenueList(models.Model):
    venue_name=models.CharField(max_length=255)
    phone = models.IntegerField()
    cover_image=models.ImageField(upload_to='media/futsal_cover',null=True)
    address =models.CharField(max_length=255)

    class Meta:
        ordering =('venue_name',)
    def __str__(self):
        return self.venue_name