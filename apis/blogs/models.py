from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



class Blog(models.Model):
   
    title =models.CharField(max_length=255)
    description = RichTextUploadingField()
    cover_image =models.ImageField(upload_to='media/blog',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
