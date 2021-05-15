from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.


class Room(models.Model):
    # (workon env)
    #  room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    available_rooms = models.IntegerField(default=100)
  
# availability = models.BooleanField(initial=True)


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField()
    rooms = models.IntegerField()
