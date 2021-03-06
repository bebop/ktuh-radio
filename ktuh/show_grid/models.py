from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime

class DJ(models.Model):
	dj_name = models.CharField(max_length=200)
	dj_email = models.EmailField(blank=True, null=True)
	dj_current_show = models.ForeignKey('Show')
	dj_user = models.ForeignKey(User, editable=False)
	dj_website = models.URLField(blank=True, null=True)
	

	def __unicode__(self):
		return self.dj_name

class Show(models.Model):
	show_name = models.CharField(max_length=255)
	show_date_added = models.DateTimeField(blank=True, null=True)
	show_image = models.ImageField(upload_to="shows", blank=True)
	show_blurb = models.CharField(max_length=255, blank=True)
	show_description = models.TextField(null=True, blank=True)
	show_user = models.ForeignKey(User, editable=True)

	def __unicode__(self):
		return self.show_name

class ShowGrid(models.Model):
	showgrid_day = models.IntegerField(editable=False)
	showgrid_time = models.IntegerField(editable=False)
	showgrid_dj = models.ForeignKey('DJ', blank=True, null=True)
