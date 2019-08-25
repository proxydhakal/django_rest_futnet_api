from django.urls import path
from apis.posts import views

urlpatterns = [
    path('',views.ListPostAPIView.as_view()),
    path('times/',views.post_time),
    path('create/',views.CreatePostAPIView.as_view()),
    path('<int:pk>/',views.SinglePostAPIView.as_view(),name='detail_post'),
    path('<int:pk>/update/',views.UpdatePostAPIView.as_view()),
    path('<int:pk>/delete/',views.DeletePostAPIView.as_view()),
    path('list_by/<str:time>/', views.PostListByTimeAPIView.as_view()),
    path('<int:pk>/comment/',views.CommentCreateAPIView.as_view()),
    # path('<int:pk>/favourite/',views.FavoriteAPIView.as_view()),
    path('<int:pk>/like/', views.NewsLikeAPIToggle.as_view(), name='like-api-toggle'),
    
]
