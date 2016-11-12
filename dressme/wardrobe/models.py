from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	zipcode = models.IntegerField()
	wardrobes = models.OneToOneField(Wardrobe)
	

	def getOutfits(date):


	def eventUtility():

	def temperatureUtility():

	def weatherUtility():




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
	inLaundry = models.BooleanField(default = False)
	daysWornBeforeWash = models.IntegerField(max_length = 1, default = 0)
	daysNotUsed = models.IntegerField(max_length = 3, default = 0)
	cloth_type = models.IntegerField(max_length = 1, choices = CLOTH_TYPES)
	cloth_name = models.IntegerField(max_length = 2, choices = CLOTH_NAMES)

	cloth_type_dict = dict(CLOTH_TYPES)
	cloth_names_dict = dict(CLOTH_NAMES)

	def get_cloth_names():
		return cloth_names_dict.values()
