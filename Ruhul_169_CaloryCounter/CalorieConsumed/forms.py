from django import forms

from CalorieConsumed.models import User,profileInfo,ConsumedCalorie

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    pass


class ProfileForm(forms.ModelForm):
    class Meta:
        model=profileInfo
        feilds='__all__'
        exclude=['user','bmr']
        
        
        
class ConsumedForm(forms.ModelForm):
    class Meta:
        model=ConsumedCalorie
        feilds='__all__'
        exclude=['consume_by']