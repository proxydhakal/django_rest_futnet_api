from django.contrib import admin
from apis.posts.models import Post,Feedback,Bookmark
# Register your models here.


admin.site.register(Post)
admin.site.register(Feedback)
admin.site.register(Bookmark)