from django import forms

from ManageCash.models import User,AddCash,Expense
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class SingupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    pass

        
class AddCashForm(forms.ModelForm):
    class Meta:
        model=AddCash
        fields='__all__'
        exclude=['user']
        
        widgets={
            'datetime':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields='__all__'
        exclude=['user']
        
        widgets={
            'datetime':forms.DateTimeInput(attrs={
                'type':'datetime-local'
            })
        }