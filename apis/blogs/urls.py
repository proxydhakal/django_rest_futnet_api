from django.urls import path
from apis.blogs import views

urlpatterns = [
    path('',views.ListBlogAPIView.as_view()),
    path('<int:pk>/',views.SingleBlogAPIView.as_view()),
    
]