from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from PIL import Image
# Create your models here.

class User(AbstractUser):
    ROLES=(("0", "Admin"), ("1", "User"), ("2", "Guest"))
    role = models.CharField(max_length=1, choices=ROLES)
    email = models.EmailField(_('email address'), unique=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS= "username", "role"

class UserProfile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    address= models.CharField(max_length=50, blank=True)
    phone =models.IntegerField(blank=True)
    profile_image=models.ImageField(default='default.jpg',upload_to='pro_picture',blank=True)
    dob= models.DateField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)


        img = Image.open(self.profile_image.path)


        if img.height > 300 or img.width> 300:
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)
