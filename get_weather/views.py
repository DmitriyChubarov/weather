import requests
import urllib.parse
import uuid
from typing import Dict, Any, Optional
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import History, City

GEOCODING_API_URL = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_API_URL = 'https://api.open-meteo.com/v1/forecast'

COOKIE_MAX_AGE = 60 * 60 * 24 * 365  

def get_user_id(request) -> str:
    user_id = request.COOKIES.get('user_id')
    if not user_id:
        user_id = str(uuid.uuid4())
    return user_id

def get_last_city(request) -> Optional[str]:
    encode_city = request.COOKIES.get('last_city')
    return urllib.parse.unquote(encode_city) if encode_city else None

def get_city_coordinates(city: str) -> tuple[float, float]:
    params = {
        'name': city,
        'count': 1,
        'language': 'en',
        'format': 'json'
    }
    
    try:
        response = requests.get(GEOCODING_API_URL, params=params)
        response.raise_for_status()
        geo_data = response.json()
        
        if not geo_data.get('results'):
            raise ValueError('Город не найден')
        
        lat=geo_data['results'][0]['latitude']
        lon=geo_data['results'][0]['longitude']
        city=geo_data['results'][0]['name']

        _, created = City.objects.get_or_create(
            city=city,
            defaults={
                'lat': lat,
                'lon': lon,
                'count': 1
            }
        )

        if not created:
            City.objects.filter(city=city).update(count=models.F('count') + 1)
            
        return (
            lat, lon
        )
    except requests.RequestException:
        raise ValueError('Ошибка при получении данных о городе')

def get_weather_data(lat: float, lon: float) -> Dict[str, Any]:
    params = {
        'latitude': lat,
        'longitude': lon,
        'current': [
            'temperature_2m',
            'relative_humidity_2m',
            'is_day',
            'windspeed_10m',
            'precipitation'
        ],
        'timezone': 'Europe/Moscow',
        'forecast_days': 1
    }
    
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise ValueError('Ошибка при получении данных о погоде')

def create_response(request, template_data: Dict[str, Any], user_id: str, city: Optional[str] = None) -> HttpResponse:
    response = render(request, 'get_weather/get_weather.html', template_data)
    response.set_cookie('user_id', user_id, max_age=COOKIE_MAX_AGE)
    
    if city:
        response.set_cookie('last_city', urllib.parse.quote(city), max_age=COOKIE_MAX_AGE)
    
    return response

def get_weather(request) -> HttpResponse:
    user_id = get_user_id(request)
    last_city = get_last_city(request)
    history = History.objects.filter(user_id=user_id).order_by('-id')[:10]
    
    if request.method == 'POST':
        city = request.POST.get('city')
        try:
            lat, lon = get_city_coordinates(city)
            weather_data = get_weather_data(lat, lon)
            History.objects.create(user_id=user_id, city=city)
            
            return create_response(
                request,
                {'data': weather_data, 'history': history},
                user_id,
                city
            )
            
        except ValueError as e:
            return create_response(
                request,
                {'error': str(e), 'history': history},
                user_id
            )
    
    return create_response(
        request,
        {'last_city': last_city, 'history': history} if last_city else {'history': history},
        user_id
    )

