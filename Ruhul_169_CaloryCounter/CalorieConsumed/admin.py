from django.contrib import admin


from CalorieConsumed.models import User,profileInfo,ConsumedCalorie
# Register your models here.

admin.site.register([User,profileInfo,ConsumedCalorie])