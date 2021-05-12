from django.db import models
from django.conf import settings

# Create your models here.


class Room(models.Model):

    #  room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    # availability = models.BooleanField(initial=True)


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    adults = models.IntegerField()
    childern = models.IntegerField()
    # rooms = models.IntegerField()
