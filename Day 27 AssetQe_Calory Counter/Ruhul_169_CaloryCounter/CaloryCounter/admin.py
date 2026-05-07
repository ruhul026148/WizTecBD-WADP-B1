from django.contrib import admin

from CaloryCounter.models import User,ProfileInfo,CalorieModel

# Register your models here.

admin.site.register([User,ProfileInfo,CalorieModel])
