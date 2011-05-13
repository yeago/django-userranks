from django.db import models

from django.core.management.base import BaseCommand

from django.contrib.auth.models import SiteProfileNotAvailable
from django.core.exceptions import ImproperlyConfigured

class Command(BaseCommand):
	def handle(self,**options):
		"""
		Basically just copied from django.contrib.auth.User.get_profile
		"""

		from django.conf import settings
		if not getattr(settings, 'AUTH_PROFILE_MODULE', False):
			raise SiteProfileNotAvailable('You need to set AUTH_PROFILE_MO'
				  'DULE in your project settings')
		try:
			app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
		except ValueError:
			raise SiteProfileNotAvailable('app_label and model_name should'
					' be separated by a dot in the AUTH_PROFILE_MODULE set'
					'ting')

		try:
			UserProfile = models.get_model(app_label, model_name)
			if UserProfile is None:
				raise SiteProfileNotAvailable('Unable to load the profile '\
					'model, check AUTH_PROFILE_MODULE in your project sett'\
					'ings')

			point_field = getattr(settings,'USERRANK_POINT_FIELD','points')

			for profile in UserProfile.objects.all():
				setattr(profile,point_field,profile.get_points())
				profile.save()
				
			for rank, i in enumerate(UserProfile.objects.order_by('-%s' % point_field)):
				i.rank_cache = rank + 1
				i.save()

			ranked_users = UserProfile.objects.filter(**{'%s__gt' % point_field: 0})

			if getattr(settings,'USERRANK_EXCLUDE_STAFF',False):
				ranked_users = ranked_users.exclude(user__is_staff=True)

			bottom = 0
			top = 0
			for i in settings.USERRANK_TIERS: # (Rank Name, percentile) aka ("Squire", .20)
				bottom = int(ranked_users.count() * (1 - i[1]))
				ranked_users.filter(rank_cache__range=(top,bottom)).update(rank_title=i[0])
				top = bottom + 1

		except (ImportError,ImproperlyConfigured):
			raise SiteProfileNotAvailable
