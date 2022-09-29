from cProfile import label
from tkinter.messagebox import NO
from unittest.mock import DEFAULT
from django.db import models
import requests

# Create your models here.

class Hotel (models.Model):
    STARS = [(1,'1*'), (2,'2*'), (3,'3*'),(4,'4*'), (5,'5*')]
    # COLLECTIONS =[('ad'='Adults Only'), ('b','Пляжная коллекция'), ('c', 'City-Break'), ('d', 'Дайвинг'), ('p', 'Pet-friendly')]        
    hotelId = models.IntegerField(blank=False, primary_key=True)
    hotelName = models.CharField(blank=False, max_length=100)
    hotelLocation = models.ForeignKey('Location', on_delete = models.CASCADE)
    hotelCountry = models.ForeignKey('Country', on_delete = models.CASCADE)
    image = models.URLField()
    stars = models.IntegerField(choices=STARS)
    collection = models.ManyToManyField('Collection')

    def __str__(self):
        return self.hotelName

    def get_hotel_photo(self):
        photo_list=[]
        for i in range (0,24):
            photo_list.append(f'https://photo.hotellook.com/image_v2/limit/h{self.hotelId}_{i}/640/480.auto')
        return photo_list
    
    def hotel_price_average(self):
        try: 
            x= requests.get(f'http://engine.hotellook.com/api/v2/cache.json?hotelId={self.hotelId}&currency=usd&checkIn=2023-02-02&checkOut=2023-02-03&limit=1&token=a6f47b425e569b83ee00e30758b1a29f')
            y = x.json()
            price = y['priceFrom']
            return f' {price} $'
        except:
            return 'N/A'
    
    def hotel_by_collection(self, collection):
        hotels = Hotel.filter(collection = collection)
        return hotels
    
class Location (models.Model):
    locationId = models.CharField(blank=False, max_length=7, primary_key=True)
    locationName = models.CharField(blank=False, max_length=100)
    country = models.ForeignKey('Country', on_delete = models.CASCADE)

    def __str__(self):
        return self.locationName


class Country (models.Model):
    countryId = models.CharField(blank=False, max_length=5, primary_key=True)
    countryName = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.countryName

class Collection (models.Model):
    collectionId = models.CharField(blank=False, max_length=7, primary_key=True)
    collectionName = models.CharField(blank=False, max_length=100)
    collectionPhoto = models.ImageField (upload_to='uploads', blank=True)

    def __str__(self):
        return self.collectionName

class Order (models.Model):
    order_id = models.AutoField
    hotel = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    checkIn = models.DateField (blank=False)
    checkOut = models.DateField (blank=False)
    adults = models.IntegerField(blank=False)
    children = models.IntegerField()
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)


def find_country2(*args):

    countries = requests.get('http://engine.hotellook.com/api/v2/static/countries.json?token=a6f47b425e569b83ee00e30758b1a29f')
    x=countries.json()
    list=[]
    for y in args:
        for i in x:
            if i['code']==y:
                list.append(i['id'])
    return list

# c = ('Мальдивы', 'ОАЭ', 'Сейшеллы', 'Доминикана', 'Маврикий', 'Франция', 'Италия', 'Испания', 'Танзания', 'Португалия')

# a = ['MV', 'AE', 'SC', 'DO', 'MU', 'FR', 'IT', 'ES', 'TZ', 'PT']
# b = find_country2(*a)
# print(b)

# countries = dict(zip(b,c))

def add_countries (**kwargs):
    for k,v in kwargs.items():
        Country.objects.create(countryId = k, countryName = v)


