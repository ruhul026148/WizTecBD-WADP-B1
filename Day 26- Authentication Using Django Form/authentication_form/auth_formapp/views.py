from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from auth_formapp.forms import RegisterForm,LoginForm
from auth_formapp.models import User

# Create your views here.

def register_page(request):
    if request.method=="POST":
       form_data=RegisterForm(request.POST)
       if form_data.is_valid:
           form_data.save()
           messages.success(request,'Registration Successfully')
           return redirect('login_page') 
    form_data=RegisterForm()
    context={
        'form_data':form_data,
        'form_title':'User Register Form',
        'form_btn':'Register'
    }
    return render(request,'master/base_form.html',context)

def login_page(request):
    if request.method=="POST":
        form_data=LoginForm(request, request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            login(request,user)
            messages.success(request,'Login SuccessFully')
            return redirect('dashboard_page')
    form_data=LoginForm()
    context={
        'form_data':form_data,
        'form_title':'User Login Form',
        'form_btn':'Login'
    }
    return render(request,'master/base_form.html',context)

def logout_page(request):
    logout(request)
    messages.success(request,'Logout SuccessFullu')
    return redirect('login_page')
    

def dashboard_page(request):
    return render(request,'dashboard.html')
