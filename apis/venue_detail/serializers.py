from rest_framework import serializers
from apis.venue_detail.models import VenueList


class FutsalListSerializer(serializers.ModelSerializer):
    class Meta:
        model =VenueList
        fields =('pk','venue_name','phone','cover_image','address',)

