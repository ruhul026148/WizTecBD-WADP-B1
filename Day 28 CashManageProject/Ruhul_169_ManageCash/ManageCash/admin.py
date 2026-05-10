from django.contrib import admin

from ManageCash.models import User,AddCash,Expense

# Register your models here.

admin.site.register([User,AddCash,Expense])