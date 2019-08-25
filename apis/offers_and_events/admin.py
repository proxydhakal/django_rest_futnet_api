from django.contrib import admin
from apis.offers_and_events.models import Event,Offer
# Register your models here.
admin.site.register(Offer)
admin.site.register(Event)