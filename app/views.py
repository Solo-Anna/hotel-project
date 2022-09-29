from random import shuffle
from django.shortcuts import render, redirect

from app.forms import SearchByCountry, SendOrder
from .models import Collection, Hotel, Country, Location, Order

def home (request):
    hotels = Hotel.objects.all()[:40]
    locations = Location.objects.all()
    countries = Country.objects.all()
    collections = Collection.objects.exclude(collectionId='hc')[:10]
    form = SearchByCountry()
    context = {'hotels': hotels,'countries' : countries, 'locations' : locations, 'collections':collections, 'form': form}
    return render (request, 'home.html', context)

def hotel (request, hotelId):
    hotel = Hotel.objects.get(hotelId = hotelId)
    photo= hotel.get_hotel_photo()
    price= hotel.hotel_price_average()
    context = {'hotel': hotel, 'photo' : photo, 'price':price}
    return render (request, 'hotel.html', context)

def hotel_search(request):
    form = SearchByCountry()

    if request.method == 'GET':
        form = SearchByCountry(request.GET, request.FILES)

        if form.is_valid():
            country = form.cleaned_data.get("query")
            results = Hotel.objects.filter(hotelCountry__countryName=country)
            # count total results
            total_results = results.count()

    return render(request,
                  'search.html', {'form': form, 'results': results, 'total_results': total_results})

def search_results (request):
    form = SearchByCountry()
    if request.method == 'GET':
        form = SearchByCountry(request.GET, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data['query']
            country = Country.objects.get(countryId = cd)
            results = Hotel.objects.filter(hotelCountry__countryId = cd)
            return render (request,'search_results.html', {'results': results, 'country' : country})
    return render (request,'home.html')

def send_order(request, hotelId):
    this_hotel = Hotel.objects.get(hotelId = hotelId)
    form = SendOrder()

    if request.method == 'POST':
        form = SendOrder(request.POST, request.FILES)

        if form.is_valid():
            # new_order = form.save(commit=False)
            # new_order.hotel = hotelId
            # new_order.save()
            # form.save_m2m()

            new_order = Order()
            new_order.checkIn= form.cleaned_data['checkIn']
            new_order.checkOut = form.cleaned_data['checkOut']
            new_order.adults = form.cleaned_data['adults']
            new_order.children = form.cleaned_data['children']
            new_order.name = form.cleaned_data['name']
            new_order.phone_number = form.cleaned_data['phone_number']
            new_order.hotel = hotelId
            new_order.save()
            return redirect('order_received')
    context = {'form':form, 'this_hotel':this_hotel, 'hotelId':hotelId}

    return render(request, 'send_order.html', context)

def order_received (request):
    return render (request, 'order_received.html')

def collections (request):
    collections = Collection.objects.exclude(collectionId='hc')[:10]
    context = {'collections':collections}
    return render (request, 'collections.html', context)

def hotels_by_collection (request, collectionId):
    collection = Collection.objects.get(collectionId = collectionId)
    hotels = Hotel.objects.filter(collection = collectionId)
    # photo= hotel.get_hotel_photo()
    # price= hotel.hotel_price_average()
    context = {'hotels': hotels, 'collection' : collection}
    return render (request, 'hotels_by_collection.html', context)
