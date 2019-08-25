from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from apis.posts import serializers
from apis.posts.models import Post
from common.permissions import IsAdminOrUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
class PostListByTimeAPIView(generics.ListAPIView):
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        return Post.objects.filter(time=self.kwargs.get('time')).order_by('-created_at')

@api_view(['GET'])
def post_time(request,*args,**kwargs):
    times=dict(Post.CHOICES)
    return Response(times,status=status.HTTP_200_OK)




class CreatePostAPIView(generics.CreateAPIView):
    authentication_classes =[authentication.JWTAuthentication,]
    permission_classes =[IsAdminOrUser]
    serializer_class = serializers.PostSerializer
    





class UpdatePostAPIView(generics.UpdateAPIView):
    authentication_classes =[authentication.JWTAuthentication,]
    permission_classes =[IsAdminOrUser]
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    



class ListPostAPIView(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    


class SinglePostAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    


class DeletePostAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes =[IsAdminOrUser]


class CommentCreateAPIView(generics.CreateAPIView):
    authentication_classes =[authentication.JWTAuthentication,]
    serializer_class = serializers.CommentSerializer
    


class UserFavoriteListAPIView(generics.ListAPIView):
    authentication_classes =[authentication.JWTAuthentication,]
    serializer_class = serializers.PostSerializer
    def get(self,request):
        user=request.user
        print(user)
        bookmarked_posts=user.bookmarks
        return Response(bookmarked_posts,status=status.HTTP_200_OK)

    
    

class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request,pk):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Post, pk=pk)
        print('obj',obj)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)


class AddFavouriteAPIToggle(APIView):
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request,pk):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Post, pk=pk)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        bookmarked = False
        if user.is_authenticated:
            if user in obj.bookmarks.all():
                bookmarked = False
                obj.bookmarks.remove(user)
            else:
                bookmarked = True
                obj.bookmarks.add(user)
            updated = True
        data = {
            "updated": updated,
            "bookmarked": bookmarked
        }
        return Response(data)


    




    

