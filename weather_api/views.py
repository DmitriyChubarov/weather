from rest_framework.generics import ListAPIView
from .serializers import CitySerializer
from get_weather.models import City

class CityGet(ListAPIView):
    queryset = City.objects.values('city', 'count') 
    serializer_class = CitySerializer
