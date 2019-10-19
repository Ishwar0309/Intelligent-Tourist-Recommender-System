from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class fileData(models.Model):
    description = models.CharField(max_length=100)
    hotelFile = models.FileField(upload_to='csvfiles')
    restaurantFile = models.FileField(upload_to='csvfiles')

class Hotel(models.Model):
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    hotelDescription = models.CharField(max_length=1000)
    hotelFacilities = models.CharField(max_length=1000)
    guestRecommendation = models.IntegerField(default=99999)
    hotelStarRating = models.IntegerField(default=3)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    siteReviewRating = models.FloatField(default=0.0)
    siteStayReviewRating = models.CharField(max_length=100,default='Good')
    pointOfInterest = models.TextField()
    propertyName = models.CharField(max_length=100)
    propertyType = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    roomType = models.CharField(max_length=100,default='Standard')
    roomFacilities = models.CharField(max_length=1000)

class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    localityVerbose = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    cuisines = models.CharField(max_length=1000,default='Indian')
    averageCostForTwo = models.IntegerField()
    aggregateRating = models.FloatField(default=0.0)
    ratingText = models.CharField(max_length=100)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    # restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

