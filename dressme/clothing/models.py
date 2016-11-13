from django.db import models
from django.contrib.auth.models import User
from datetime import date
import requests
from geopy.geocoders import Nominatim

WEATHERURL = "http://api.openweathermap.org/data/2.5/forecast"


# Create your models here.
class Wardrobe(models.Model):
	CLOTH_TYPES = (
		(1, "TOP"),
		(2, "BOTTOM"),
		(3, "JACKET"),
		(4, "ACCESSORY")
		)
	CLOTH_NAMES = (
		(1, "T-SHIRT"),
		(2, "POLO"),
		(3, "BUTTONED_SHIRT"),
		(4, "JEANS"),
		(5, "SHORTS"),
		(6, "SWEATS"),
		(7, "COAT"),
		(8, "HOODIE"),
		(9, "SWEATER"),
		(10, "EARMUFFS"),
		(11, "UMBRELLA"),
		(12, "SCARF"),
		(13, "GLOVES"),
		)
	CLOTH_WEATHER = (
		(1, "Cold"),
		(2, "Chilly"),
		(3, "Mild"),
		(4, "Warm"),
		(5, "Hot"))

	inLaundry = models.BooleanField(default = False)
	daysWornBeforeWash = models.IntegerField(default = 0)
	daysNotUsed = models.IntegerField(default = 0)
	cloth_type = models.IntegerField(choices = CLOTH_TYPES)
	cloth_name = models.IntegerField(choices = CLOTH_NAMES)
	cloth_weather = models.IntegerField(choices = CLOTH_NAMES)

	cloth_type_dict = dict(CLOTH_TYPES)
	cloth_names_dict = dict(CLOTH_NAMES)

	def get_cloth_names():
		return cloth_names_dict.values()
		
class StormChaser(User):
	city = models.CharField(max_length = 30)
	state = models.CharField(max_length = 2)
	#wardrobes = models.OneToOneField(Wardrobe)
	

	def getOutfits(self):
		api_id = '329ece2a6e7bcf2ad488f635b21588d0'
		geolocator = Nominatim()
		location = geolocator.geocode(self.city + ", " + self.state)	
		latitude = location.latitude
		longitude = location.longitude
		data = requests.get(WEATHERURL, params = dict(lat = latitude, lon = longitude, units = 'imperial', APPID = api_id))
		data_dict = data.json()
		five_day_forecast = data_dict.get('list')
		one_day_forecast = five_day_forecast[0:7]
		worstWeather = getWorstWeather(one_day_forecast)

	def getWorstWeather(day_forecasts):
		weathers = set([day_forecasts[i].get('weather').get('description') for i in range(7)])

	def getAvgTemp(day_forecasts):
		 return sum([day_forecasts[i].get('main').get('temp') for i in range(7)]) / 7.0


	def eventUtility(self):
		pass

	def temperatureUtility(self, tempeature):
		pass

	def weatherUtility(self, weather):
		pass