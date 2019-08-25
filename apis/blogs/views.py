from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from apis.blogs import serializers
from apis.blogs.models import Blog

# Create your views here.

class ListBlogAPIView(generics.ListAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogListSerializer


class SingleBlogAPIView(generics.RetrieveAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogListSerializer
   