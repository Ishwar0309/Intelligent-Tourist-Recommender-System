
import pandas as pd
df = pd.read_csv('restaurants.csv')

for i,g in df.groupby('Country Code'):
	if i == 1:
		df = g

print(df.head())

prefferedStyles = [' North Indian', 'Chinese', ' Mughlai', 'Cafe']
prefferedPrice = 1200
cuisineScore = {}
for index, row in df.iterrows():
	matchedStyles = 0
	averageCostForTwo = int(row['Average Cost for two'])
	print(averageCostForTwo)
	if type(row['Cuisines']) == str:
		cuisineStyle = row['Cuisines'].split(',')
		for cuisines in cuisineStyle:
			if cuisines in prefferedStyles:
				matchedStyles = matchedStyles + 1
	difference = prefferedPrice - averageCostForTwo
	if difference < 0 :
		difference = difference * -1
	score = 100*matchedStyles - difference
	cuisineScore[row['Restaurant Name']] = score

print(cuisineScore)
cuisinesTop = sorted(cuisineScore.items(), key = 
             lambda kv:(-kv[1], kv[0]))

return cuisinesTop[:12]

# return cuisinesTop[:12]
	# if type(row['room_facilities']) == str:
	# 	facilitiesAvailable = row['room_facilities'].split('|')
	# 	for facility in facilitiesAvailable:
	# 		if facility in roomFacScore.keys():
	# 			roomFacScore[facility] = roomFacScore[facility] + 1
	# 		else :
	# 			roomFacScore[facility] = 1

	# if type(row['hotel_facilities']) == str:
	# 	facilitiesAvailable = row['hotel_facilities'].split('|')
	# 	for facility in facilitiesAvailable:
	# 		if facility in hotelFacScore.keys():
	# 			hotelFacScore[facility] = hotelFacScore[facility] + 1
	# 		else:
	# 			hotelFacScore[facility] = 1
				




	


# displayFacilitesHotel = sorted(hotelFacScore.items(), key = 
#              lambda kv:(-kv[1], kv[0]))

# return displayFacilitesHotel[:12],displayFacilitesRoom[:12]














