import numpy
from math import radians, sin, cos, acos

class Analysis:
	def calculateDistance(self,slat,slon,elat,elon):
		slat = radians(float(slat))
		slon = radians(float(slon))
		elat = radians(float(elat))
		elon = radians(float(elon))
		dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
		return dist

	def HotelRecommendations(self,room_facilities,hotel_facilities,property_type='Hotel',state = 'Maharashtra'):
		import pandas as pd
		df = pd.read_csv('media/csvfiles/goIbibo.csv')

		for i, g in df.groupby('state'):
			if i == state:
				df = g
				for j, h in df.groupby('property_type'):
					if j == property_type:
						df = h

		score_dictionary = {}

		for index, row in df.iterrows():
			matchedRoomFacilities = 0
			matchedHotelFacilities = 0

			if type(row['room_facilities']) == str:
				facilitiesAvailable = row['room_facilities'].split('|')
				for facility in facilitiesAvailable:
					if facility in room_facilities:
						matchedRoomFacilities = matchedRoomFacilities + 1

			if type(row['hotel_facilities']) == str:
				facilitiesAvailable = row['hotel_facilities'].split('|')
				for facility in facilitiesAvailable:
					if facility in hotel_facilities:
						matchedHotelFacilities = matchedHotelFacilities + 1

			score = (matchedHotelFacilities ** 2 + matchedRoomFacilities ** 2) ** 0.5
			print(score)
			score_dictionary[row['property_name']] = score

		recommendations = sorted(score_dictionary.items(), key=
		lambda kv: (-kv[1], kv[0]))

		return recommendations[:7]

	def displayData(self):
		import pandas as pd
		df = pd.read_csv('media/csvfiles/goIbibo.csv')
		hotelFacScore = {}
		roomFacScore = {}
		for index, row in df.iterrows():

			if type(row['room_facilities']) == str:
				facilitiesAvailable = row['room_facilities'].split('|')
				for facility in facilitiesAvailable:
					if facility in roomFacScore.keys():
						roomFacScore[facility] = roomFacScore[facility] + 1
					else:
						roomFacScore[facility] = 1

			if type(row['hotel_facilities']) == str:
				facilitiesAvailable = row['hotel_facilities'].split('|')
				for facility in facilitiesAvailable:
					if facility in hotelFacScore.keys():
						hotelFacScore[facility] = hotelFacScore[facility] + 1
					else:
						hotelFacScore[facility] = 1

		displayFacilitesRoom = sorted(roomFacScore.items(), key=
		lambda kv: (-kv[1], kv[0]))

		displayFacilitesHotel = sorted(hotelFacScore.items(), key=
		lambda kv: (-kv[1], kv[0]))

		return displayFacilitesHotel[:13], displayFacilitesRoom[:13]














