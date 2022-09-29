from django.core.management.base import BaseCommand
from app.models import Hotel, Location, Collection
import requests

class Command(BaseCommand):
    help = 'Добавить отели'

    def add_arguments(self, parser):
        parser.add_argument('locationId', type=str, help=u'Id Локации')
        # parser.add_argument('countryId', type=str, help=u'Id Локации')
        # parser.add_argument('stars', type=str, help=u'Звездность отеля')
        # parser.add_argument('total', type=int, help=u'Количество создаваемых отелей')

    def handle(self, *args, **kwargs):
        # total = kwargs['total']
        locationId = kwargs['locationId']
        new_Location = Location.objects.get(locationId = locationId)
        ad = Collection.objects.get(collectionId="ad")
        # countryId= kwargs ['countryId']
        # stars = kwargs['stars']
        response = requests.get(f'http://engine.hotellook.com/api/v2/static/hotels.json?locationId={locationId}&limit=100&token=a6f47b425e569b83ee00e30758b1a29f')
        hotels = response.json()
        for i in hotels['hotels']:
            if 148 in i['facilities'] and i['stars']==4:
                new_hotel = Hotel (hotelName = i['name']['en'], hotelId = i['id'], image = i['photos'][0]['url'], stars = 4, hotelLocation = new_Location, hotelCountry=new_Location.country)
                new_hotel.collection.add(ad)
                new_hotel.save()