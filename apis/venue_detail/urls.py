from django.urls import path
from apis.venue_detail import views

urlpatterns = [
    path('lists/',views.ListVenueAPIView.as_view()),
    path('list/<int:pk>/',views.SingleVenueAPIView.as_view()),
    
]