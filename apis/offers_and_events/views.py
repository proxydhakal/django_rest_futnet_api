from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import permissions
from apis.offers_and_events import serializers
from apis.offers_and_events.models import Offer,Event
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ListOfferAndOfferPIView(APIView):
    
    def get(self,request):
        offer_serializer=serializers.OfferSerailizer(many=True)
        event_serailizer=serializers.EventSerializer(many=True)
        response_data={"offers":offer_serializer.data,"events":event_serailizer.data}
        print(response_data)
        return Response(response_data,status=status.HTTP_200_OK)


class SingleOfferAPIView(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = serializers.OfferSerailizer


class SingleEventAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer

   