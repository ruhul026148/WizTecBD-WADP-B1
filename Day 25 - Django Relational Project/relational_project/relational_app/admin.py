from django.contrib import admin

from relational_app.models import CustomUserInfoModel,ProfileModel,ProductModel

# Register your models here.
admin.site.register([CustomUserInfoModel,ProfileModel,ProductModel])