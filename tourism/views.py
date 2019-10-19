from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tourism.models import *
import pandas as pd
from django.views.generic import DetailView
from .models import Hotel
from django.urls import reverse



# Create your views here.
@login_required
def base(request):
    return render(request,"tourism/base.html")

@login_required
def profile(request):
    return render(request,"tourism/profile.html")

@login_required
def home(request):
	return render(request,"tourism/home.html" , {'queryset':Hotel.objects.all()[:100]} )


class HotelDetailView(DetailView):
	model = Hotel

def DetailView(request,pk):
    hotel = Hotel.objects.get(pk = pk)
    return render()

def cart(request):
    print('hey')
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        print('post')
        details = request.POST
        id = int(details['hotelId'])
        hotel = Hotel.objects.get(pk = id)
        print(hotel)
        print(user)
        cart = Cart(hotel=hotel,user=user)
        print(cart)
        cart.save()
    cartItems = Cart.objects.filter(user = user)
    print(cartItems)
    return render(request,'tourism/cart.html',{'cart':cartItems})

def deleteItem(request,pk):
    print('gayaddddddddddddddddddddddddddddddddddddddddddddddd3333333333##############################')
    print(pk)
    user = User.objects.get(username=request.user)
    hotel = Hotel.objects.get(pk = pk)
    cart = Cart.objects.filter(hotel=hotel)
    cart.delete()
    cartItems = Cart.objects.filter(user=user)
    # return redirect(reverse('cart:cartIte'))
    return render(request,'tourism/cart.html',{'cart':cartItems})
def upload(request):
    try:
        print('hey')
        files = fileData.objects.all()
        hotelfile = pd.read_csv(files[0].hotelFile.path)
        restaurantFile = pd.read_csv(files[0].restaurantFile.path)
        print(hotelfile.columns)
        isCode = restaurantFile['Country Code']==1
        restaurantFile = restaurantFile[isCode]
        print(restaurantFile.columns)
        # Iterate through dataframe
        for index,rows in hotelfile.iterrows():
            print('heylo')
            address = rows['address']
            area = rows['area']
            city = rows['city']
            guestRecommendation = rows['guest_recommendation']
            hotelDescription = rows['hotel_description']
            hotelFacilities = rows['hotel_facilities']
            hotelStarRating = rows['hotel_star_rating']
            locality = rows['locality']
            latitude = rows['latitude']
            longitude = rows['longitude']
            pointsOfInterest = rows['point_of_interest']
            propertyName = rows['property_name']
            propertyType = rows['property_type']
            province = rows['province']
            roomFacilities = rows['room_facilities']
            roomType = rows['room_type']
            siteReviewRating = rows['site_review_rating']
            siteStayReviewRating = rows['site_stay_review_rating']
            state = rows['state']
            print(state)
            try:
                hotel = Hotel(address=address,area=area,city=city,guestRecommendation=guestRecommendation,
                              hotelDescription=hotelDescription,hotelFacilities=hotelFacilities,hotelStarRating=hotelStarRating,
                              locality=locality,latitude=latitude,longitude=longitude,pointOfInterest=pointsOfInterest,propertyName=propertyName,
                              propertyType=propertyType,province=province,roomFacilities=roomFacilities,roomType=roomType,siteReviewRating=siteReviewRating,
                              siteStayReviewRating=siteStayReviewRating,state = state)
                hotel.save()
            except Exception as e:
                print('gaya')
                print(e)

        for index,rows in restaurantFile.iterrows():
            print('hey')
            restaurantName = rows['Restaurant Name']
            city = rows['City']
            address = rows['Address']
            locality = rows['Locality']
            localityVerbose = rows['Locality Verbose']
            longitude = rows['Longitude']
            latitude = rows['Latitude']
            cuisines = rows['Locality']
            averageCostForTwo = rows['Average Cost for two']
            aggregateRating = rows['Aggregate rating']
            ratingText = rows['Rating text']
            try:
                restaurant = Restaurant(restaurantName=restaurantName,city=city,address=address,
                              locality=locality,localityVerbose=localityVerbose,longitude=longitude,latitude=latitude,cuisines=cuisines,
                              averageCostForTwo=averageCostForTwo,aggregateRating=aggregateRating,ratingText=ratingText)
                restaurant.save()
            except Exception as e:
                print(e)
    except Exception as e:
        print('ismein gaya')
        print(e)

    return render(request,"tourism/upload.html")
