from django.urls import path
from apis.offers_and_events import views

urlpatterns = [
    path('',views.ListOfferAndOfferPIView.as_view()),
    path('<int:pk>/offer',views.SingleOfferAPIView.as_view()),
    path('<int:pk>/event',views.SingleEventAPIView.as_view()),
    
]