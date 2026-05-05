from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from auth_formapp.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    class Meta:
        pass
