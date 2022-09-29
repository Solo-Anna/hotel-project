from django.core.management.base import BaseCommand
from app.models import Hotel, Location, Collection
import requests

class Command(BaseCommand):
    help = 'Добавить отели'

    def add_arguments(self, parser):
        parser.add_argument('locationId', type=str, help=u'Id Локации')

    def handle(self, *args, **kwargs):
        # total = kwargs['total']
        locationId = kwargs['locationId']
        new_Location = Location.objects.get(locationId = locationId)
        pc = Collection.objects.get(collectionId="pc")
        response = requests.get(f'http://engine.hotellook.com/api/v2/static/hotels.json?locationId={locationId}&limit=100&token=a6f47b425e569b83ee00e30758b1a29f')
        hotels = response.json()
        for i in hotels['hotels']:
            if 28 in i['facilities'] and i['stars']==5:
                new_hotel = Hotel (hotelName = i['name']['en'], hotelId = i['id'], image = i['photos'][0]['url'], stars = 5, hotelLocation = new_Location, hotelCountry=new_Location.country)
                new_hotel.collection.add(pc)
                new_hotel.save()