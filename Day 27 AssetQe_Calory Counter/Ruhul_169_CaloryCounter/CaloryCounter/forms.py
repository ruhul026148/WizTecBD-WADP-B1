
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from CaloryCounter.models import User,CalorieModel,ProfileInfo

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    pass


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileInfo
        fields ='__all__'
        exclude=['user','bmr']