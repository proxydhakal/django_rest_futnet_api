from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from apis.venue_detail import serializers
from apis.venue_detail.models import VenueList

# Create your views here.

class ListVenueAPIView(generics.ListAPIView):
    
    queryset = VenueList.objects.all()
    serializer_class = serializers.FutsalListSerializer


class SingleVenueAPIView(generics.RetrieveAPIView):
    
    queryset = VenueList.objects.all()
    serializer_class = serializers.FutsalListSerializer
   