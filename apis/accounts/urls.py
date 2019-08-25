from django.urls import path
from apis.accounts import views

urlpatterns = [
    path("users/create/",views.CreateUserView.as_view()),
    path("users/list/",views.UserListView.as_view()),
    path("users/<int:pk>/delete/",views.DeleteUserView.as_view()),
    path("users/<int:pk>/update/",views.UpdateUserView.as_view()),
    path("users/<int:pk>/posts/",views.user_posts),
    
]