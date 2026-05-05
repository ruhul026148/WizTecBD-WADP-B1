from django import forms
from relational_app.models import CustomUserInfoModel,ProfileModel,ProductModel

class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields='__all__'
        exclude=['user']
        
        widgets={
            'dob':forms.DateInput(attrs={
                'type':'date'
            })
        }
        

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields='__all__'
        exclude=['total_amount','created_by']
    