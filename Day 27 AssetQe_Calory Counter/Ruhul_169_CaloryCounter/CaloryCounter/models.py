from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    
    def __str__(self):
        return f'{self.username}'
    
    # Create a django-form to take input Name, Age, Gender, Height, Weight etc.
class ProfileInfo(models.Model):
    GRNDER=[
        ('Male','Male'),
        ('Female','Female'),
    ]
        
    
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_info',null=True)
    name=models.CharField(max_length=100,null=True)
    age=models.PositiveIntegerField(null=True)
    gender=models.CharField(max_length=30,choices=GRNDER ,null=True)
    height=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    bmr=models.FloatField(null=True)
    
    def __str__(self):
        return f'{self.name}-{self.age}'

#Item name, Calorieconsumed
class CalorieModel(models.Model):
    item_name=models.CharField(max_length=100,null=True)
    Calorie_consumed=models.FloatField(null=True)
    created_at=models.DateField(auto_now_add=True,null=True)
    consumed_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_calorie',null=True)
    
    def __str__(self):
        return f'{self.item_name}-{self.consumed_by.username}'
    