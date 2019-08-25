from rest_framework import serializers
from apis.offers_and_events.models import Offer,Event



class OfferSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields=('pk','title','detail','cover_image','venue')



class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields =('pk','title','detail','cover_image','location','date_time')