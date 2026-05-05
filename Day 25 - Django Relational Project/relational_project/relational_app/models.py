from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserInfoModel(AbstractUser):
    
    USER_TYPE=[
        ('Seller','Seller'),
        ('Buyer','Buyer')
    ]

    full_name=models.CharField(max_length=100,null=True)
    user_type=models.CharField(max_length=20,choices=USER_TYPE,null=True)
    
    def __str__(self):
        return f'{self.full_name}-{self.username}'
    
class ProfileModel(models.Model):
    user=models.OneToOneField(CustomUserInfoModel,on_delete=models.CASCADE,related_name='user_profile',null=True)
    address=models.TextField(null=True)
    contact=models.CharField(max_length=30,null=True)
    dob=models.DateField(null=True)
    profile_image=models.ImageField(upload_to='Image',null=True)
    
    def __str__(self):
        return f'{self.user}'
    
class ProductModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    qty=models.PositiveIntegerField(null=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    created_by=models.ForeignKey(CustomUserInfoModel,on_delete=models.CASCADE,related_name='user_product',null=True)
    
    created_at = models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    
    def __str__(self):
        return f'{self.name}'