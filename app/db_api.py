import requests

# поиск кода страны в словарь
def find_country2(*args):

    countries = requests.get('http://engine.hotellook.com/api/v2/static/countries.json?token=a6f47b425e569b83ee00e30758b1a29f')
    x=countries.json()
    list=[]
    for y in args:
        for i in x:
            if i['code']==y:
                list.append(i['id'])
    return list

# поиск отелей по локации
def hotel_search(locationId):
    response = requests.get(f'http://engine.hotellook.com/api/v2/static/hotels.json?locationId={locationId}&limit=20&token=a6f47b425e569b83ee00e30758b1a29f')
    hotels = response.json()
    hotel_list=[]
    for i in hotels['hotels']:
        if i['stars']==5:
            hotel_list.append(([i['name']['en'], i['id'], i['photos'][0]['url'], i['stars']]))
    return hotel_list

# поиск отелей в локации
def hotel_list(locationId):
    response = requests.get(f'http://engine.hotellook.com/api/v2/static/hotels.json?locationId={locationId}&limit=100&token=a6f47b425e569b83ee00e30758b1a29f')
    hotels = response.json()
    return hotels


# поиск отеля в локации по названию
def hotel_search(locationId, name):
    hotels=(hotel_list(locationId))
    for i in hotels['hotels']:
        if name in i['name']['en']:
            print (i['name']['en'], i['id'], i['photos'][1]['url'], i['stars'])

# поиск отеля в локации по услуге:
def hotel_search2(locationId, facility):
    hotels=(hotel_list(locationId))
    for i in hotels['hotels']:
        if facility in i['facilities'] and i['stars']==5:
            print (i['name']['en'], i['id'], i['photos'][1]['url'], i['stars'])

# 65 = спа, 148 = adults only, 28 с животными
# find_country2('MV')

print(hotel_search(14003, 'Dianella'))