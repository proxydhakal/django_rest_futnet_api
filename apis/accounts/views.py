from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from apis.accounts.models import User
from common.permissions import UserIsOwnerOrReadOnly,IsAdminOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apis.accounts.serializers import CreateUserSerializer, UpdateUserSerailizer,UserListSerializer,UserPostSerializer
# Create your views here.

@api_view(['GET'])
def user_posts(request, *args, **kwargs):
    user = get_object_or_404(User,pk=kwargs.get('pk'))
    serializer = UserPostSerializer(user)
    return Response(serializer.data,status=status.HTTP_200_OK)


class UserListView(generics.ListAPIView):
    queryset= User.objects.all()
    serializer_class=UserListSerializer
    permission_classes= (permissions.IsAuthenticated,IsAdminOnly)

class CreateUserView(generics.CreateAPIView):
    serializer_class =CreateUserSerializer
    permission_classes = (permissions.AllowAny,)



class UpdateUserView(generics.UpdateAPIView):
    serializer_class= UpdateUserSerailizer
    permission_classes= (permissions.IsAuthenticated,UserIsOwnerOrReadOnly)
    queryset= User.objects.all()

class DeleteUserView(generics.DestroyAPIView):
    permission_classes= (permissions.IsAuthenticated,UserIsOwnerOrReadOnly)
    queryset= User.objects.all()


