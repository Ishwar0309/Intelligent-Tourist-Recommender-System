from math import radians, sin, cos, acos

class Analysis:
	def calculateDistance(slat,slon,elat,elon):
		slat = radians(float(slat))
		slon = radians(float(slon))
		elat = radians(float(elat))
		elon = radians(float(elon))
		dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
		return dist