from django.contrib import admin
from django.contrib.auth.models import User
from faq.models import Faq
from models import *
import datetime


admin.site.register(Faq)
