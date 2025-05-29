from django.db import models

class History(models.Model):
    user_id = models.TextField()
    city = models.CharField(max_length=255)

    class Meta:
        db_table='history'

    def __str__(self):
        return self.user_id
    
class City(models.Model):
    city = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    count = models.IntegerField()

    class Meta:
        db_table='city'

    def __str__(self):
        return self.city
