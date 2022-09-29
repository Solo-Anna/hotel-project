from django.contrib import admin
from .models import Collection, Hotel, Country, Location, Order

admin.site.register(Hotel)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(Order)
admin.site.register(Collection)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('collectionId', 'colletionName')

# Register your models here.
