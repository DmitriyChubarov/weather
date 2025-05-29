from rest_framework import serializers
from get_weather.models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city', 'count']