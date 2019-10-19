from django.db import models
from mapbox_location_field.models import LocationField,AddressAutoHiddenField

class Location(models.Model):
	location = LocationField()
	# address = AddressAutoHiddenField()

