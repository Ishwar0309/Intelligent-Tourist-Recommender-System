from django.shortcuts import render
from cities import forms
from tourism.models import Hotel,Restaurant
from cities.scripts.nearestPoints import Analysis

# Create your views here.
def index(request):
	if request.method == 'POST':
		data = request.POST
		location = request.POST['location']
		locations = location.split(',')
		latitude = locations[0]
		longitude = locations[1]
		object = Analysis()
		cityList = []
		for hotel in Hotel.objects.all():
			elat = hotel.latitude
			elon = hotel.longitude
			distance = object.calculateDistance(latitude,longitude,elat,elon)
			cityList.append((hotel.id,distance))
			print(distance)
		cityList = sorted(cityList, key = lambda x: x[1])
		finalList = []
		instance = forms.LocationForm()
		counter = 0
		for hotels in cityList:
			if counter<6:
				finalList.append(hotels[0])
			counter = counter + 1
		print(finalList)
		return render(request,'cities/map.html',{'form':instance,'queryset':Hotel.objects.filter(id__in = finalList)})
	instance = forms.LocationForm()
	return render(request,'cities/map.html',{'form':instance,'queryset':Hotel.objects.all()[:12]})


def submitInfo(request):
	if request.method == 'POST':
		print(request.POST)
		location = request.POST['location']
		print(type(location))
		latitude = location[0]
		longitude = location[1]
		print(type(latitude))
		print(latitude)
		instance = forms.LocationForm()
		return render(request,'cities/map.html',{'form':instance})


def recommend(request):
	object = Analysis()
	hotelFacilites, roomFacilites = object.displayData()
	cuisineStyles = object.displayCuisineData()
	hotelFacilites = dict(hotelFacilites)
	roomFacilites = dict(roomFacilites)
	cuisineStyles = dict(cuisineStyles)
	counter = 0
	hotelNewFacilities = []
	temp = {}
	for key, values in hotelFacilites.items():
		keyNew = 'facilityHotel' + str(counter)
		temp[keyNew] = key
		counter = counter + 1
	counter = 0
	for key, values in roomFacilites.items():
		keyNew = 'facilityRoom' + str(counter)
		temp[keyNew] = key
		counter = counter + 1
	counter = 0
	for key, values in cuisineStyles.items():
		keyNew = 'cuisineStyles' + str(counter)
		temp[keyNew] = key
		counter = counter + 1
	if request.method == "POST":
		print('hhhh')
		preferredRoomFacilites = request.POST.getlist('facilityRoom')
		preferredHotelFacilites = request.POST.getlist('facilityHotel')
		preferredCuisineSyles = request.POST.getlist('cuisineStyles')
		priceForTwo = request.POST.get('rangePick')
		print(priceForTwo)
		cuisineRecommendations = object.recommendCuisine(prefferedPrice=int(priceForTwo),prefferedStyles=preferredCuisineSyles)
		recommendations = object.HotelRecommendations(room_facilities=preferredRoomFacilites,hotel_facilities=preferredHotelFacilites)
		restNames = []
		hotelNames = []
		for recommenda in recommendations:
			hotelNames.append(recommenda[0])
		for recom in cuisineRecommendations:
			restNames.append(recom[0])
		hotels = Hotel.objects.filter(propertyName__in = hotelNames)
		restaurants = Restaurant.objects.filter(restaurantName__in = restNames)
		print(restNames)
		return render(request, 'cities/recommend.html', {'queryset':hotels,'temp':temp,'posted':1,'restaurants':restaurants})

	return render(request,'cities/recommend.html',{'temp':temp})





