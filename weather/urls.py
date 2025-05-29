
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('get_weather/', include('get_weather.urls')),
   path('weather_api/', include('weather_api.urls')),
]

