from django.contrib import admin
from apis.accounts.models import UserProfile,User
# Register yfromour models here.
admin.site.register(User)
admin.site.register(UserProfile)