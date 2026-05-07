from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    
    def __str__(self):
        return f'(self.username)'
    
class profileInfo(models.Model):
    GENDER=[
        ('Male','Male'),
        ('Female','Female')
        
    ]
    
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='auth_user',null=True)
    name=models.CharField(max_length=100,null=True)
    age=models.PositiveIntegerField(null=True)
    gender=models.CharField(max_length=30,choices=GENDER,null=True)
    height=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    bmr=models.FloatField(null=True)
    
    def __str__(self):
        return f'{self.name}'
    
    
class ConsumedCalorie(models.Model):
    item_name=models.CharField(max_length=100,null=True)
    claorie_consume=models.FloatField(null=True)
    created_at=models.DateField(auto_now_add=True,null=True)
    consume_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='calorie_consume',null=True)
    
    
    
    def __str__(self):
        return f'{self.item_name}-{self.consume_by.username}'