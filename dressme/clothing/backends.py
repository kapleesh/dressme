from django.conf import settings
from .models import *

class CustomBackend(object):
	def authenticate(self, username=None, password=None):
		try:
			user = None
			user = StormChaser.objects.get(username=username)
			if user.check_password(password):
				return user 
		except StormChaser.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return StormChaser.objects.get(pk=user_id)
		except StormChaser.DoesNotExist:
			return None