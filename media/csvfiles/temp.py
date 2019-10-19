import pandas as pd
df = pd.read_csv('goIbibo.csv')


score_dictionary = {}
totalFacilities = []
hotelFacScore = {}
roomFacScore = {}
for index, row in df.iterrows():
	matchedRoomFacilities = 0
	matchedHotelFacilities = 0

	if type(row['room_facilities']) == str:
		facilitiesAvailable = row['room_facilities'].split('|')
		for facility in facilitiesAvailable:
			if facility in roomFacScore.keys():
				roomFacScore[facility] = roomFacScore[facility] + 1
			else :
				roomFacScore[facility] = 1

	if type(row['hotel_facilities']) == str:
		facilitiesAvailable = row['hotel_facilities'].split('|')
		for facility in facilitiesAvailable:
			if facility in hotelFacScore.keys():
				hotelFacScore[facility] = hotelFacScore[facility] + 1
			else:
				hotelFacScore[facility] = 1
				




	
displayFacilitesRoom = sorted(roomFacScore.items(), key = 
             lambda kv:(-kv[1], kv[0]))

displayFacilitesHotel = sorted(hotelFacScore.items(), key = 
             lambda kv:(-kv[1]: kv[0]))

return displayFacilitesHotel[:12],displayFacilitesRoom[:12]














