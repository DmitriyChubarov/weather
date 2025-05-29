from django.urls import path
from . import views

urlpatterns = [
    path('', views.CityGet.as_view(), name='get_weather'),
]

