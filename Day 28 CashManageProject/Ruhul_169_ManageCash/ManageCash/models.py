from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    def __str__(self):
        return f'{self.username}'
    
class AddCash(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_cash',null=True)
    source=models.CharField(max_length=200,null=True)
    datetime=models.DateTimeField(null=True)
    amount=models.FloatField(null=True)
    description=models.TextField(null=True)
    
    def __str__(self):
        return f'{self.source}'
    
    
class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_expense',null=True)
    description=models.TextField(null=True)
    amount=models.FloatField(null=True)
    datetime=models.DateTimeField(null=True)
    
    def __str__(self):
        return f'{self.description}'
    
    
    
    

