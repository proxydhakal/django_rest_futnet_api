from rest_framework import serializers
from apis.blogs.models import Blog


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model =Blog
        fields =('pk','title','description','cover_image','created_at',)

