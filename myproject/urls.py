"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views as app_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('', app_views.home, name = 'home'),
    path ('search_results/', app_views.search_results, name='search_results'),
    path ('hotel/<int:hotelId>/', app_views.hotel, name = 'hotel'),
    path ('collections/<collectionId>/', app_views.hotels_by_collection, name = 'hotels_by_collection'),    
    path ('collections', app_views.collections, name = 'collections'),
    path ('hotel/<int:hotelId>/send_order/', app_views.send_order, name = 'send_order'),
    path ('order_received', app_views.order_received, name = 'order_received')

]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)