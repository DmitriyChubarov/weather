from django.conf.urls import url
from . import views

#urlpatterns = [
#    path('', views.get_weather, name='get_weather'),
#]
urlpatterns = [
    url(r'^', views.CityGet.as_view(), name='weather_api'),
]
