from django.contrib.sites.models import Site
import datetime

def current_time(request):
	try:
		time = datetime.datetime.now().strftime("%b %d %H:%M")
		return {
			'current_time': time,
		}
	except Site.DoesNotExist:
		return {'current_time':''} # an empty string
