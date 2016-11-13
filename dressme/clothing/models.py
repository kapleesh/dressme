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
		(11, "SCARF"),
		(12, "GLOVES"),
		)
	CLOTH_WEATHER = (
		(1, "Cold"),
		(2, "Chilly"),
		(3, "Mild"),
		(4, "Warm"),
		(5, "Hot"))

	in_laundry = models.BooleanField(default = False)
	for_cold = models.BooleanField(default = False)
	for_chilly = models.BooleanField(default = False)
	for_mild = models.BooleanField(default = False)
	for_warm = models.BooleanField(default = False)
	for_hot = models.BooleanField(default = False)
	daysWornBeforeWash = models.IntegerField(default = 0)
	daysNotUsed = models.IntegerField(default = 0)
	cloth_type = models.IntegerField(choices = CLOTH_TYPES)
	cloth_name = models.IntegerField(choices = CLOTH_NAMES)
	cloth_weather = models.IntegerField(choices = CLOTH_WEATHER)

	cloth_type_dict = dict(CLOTH_TYPES)
	cloth_names_dict = dict(CLOTH_NAMES)

	def get_cloth_names():
		return cloth_names_dict.values()
		
class StormChaser(User):
	city = models.CharField(max_length = 30, blank=True)
	state = models.CharField(max_length = 2, blank=True)
	wardrobe = models.OneToOneField(Wardrobe)
	

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
		temp = getAvgTemp(one_day_forecast)
		return self.weatherTempUtility(temp, worstWeather)

	def getWorstWeather(day_forecasts):
		weathers = set([day_forecasts[i].get('weather').get('description') for i in range(7)])

	def getAvgTemp(day_forecasts):
		 return sum([day_forecasts[i].get('main').get('temp') for i in range(7)]) / 7.0


	def eventUtility(self):
		pass

	def temperatureUtility(self, temperature, weather):
		def getAllClothTypes(possible_clothes):			
			tops = possible_clothes.objects.filter(cloth_type=1)
			bottoms = possible_clothes.objects.filter(cloth_type=2)
			jackets = possible_clothes.objects.filter(cloth_type=3)
			accessories = possible_clothes.objects.filter(cloth_type=4)
			return {"tops": tops, "bottoms": bottoms, "jackets": jackets, "accessories": accessories}


		weather_type = 0

		if temperature <= 55:
			possible_clothes = wardrobe.objects.filter(for_cold=True, in_laundry=False)
			weather_type = 1
		elif temperature <= 68:
			possible_clothes = wardrobe.objects.filter(for_chilly=True, in_laundry=False)
			weather_type = 2
		elif temperature <= 78:
			possible_clothes = wardrobe.objects.filter(for_mild=True, in_laundry=False)
			weather_type = 3
		elif temperature <= 85:
			possible_clothes = wardrobe.objects.filter(for_warm=True, in_laundry=False)
			weather_type = 4
		else: 
			possible_clothes = wardrobe.objects.filter(for_hot=True, in_laundry=False)
			weather_type = 5

		
		organized_possible = getAllClothTypes(possible_clothes)







	def weatherUtility(self, weather):
		pass