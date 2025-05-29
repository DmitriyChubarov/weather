
from django.contrib import admin
from django.conf.urls import url, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('get_weather/', include('get_weather.urls')),
#]
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_weather/', include('get_weather.urls')),
    url(r'^weather_api/', include('weather_api.urls')),
]
