from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout

from CaloryCounter.models import User,ProfileInfo,CalorieModel

from CaloryCounter.forms import RegistrationForm,LoginForm,UserProfileForm

# Create your views here.

def singup_page(request):
    if request.method == "POST":
        form_data=RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Registration SuccessFully')
            return redirect('login_page')
    form_data=RegistrationForm()
    context={
        'form_data':form_data
    }
    return render(request,'master/base-form.html',context)

def login_page(request):
    if request.method == "POST":
        form_data=LoginForm(request, request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            login(request, user)
            messages.success(request,'Login SuccessFully')
            return redirect('dashboard_page')
    form_data=LoginForm()
    context={
        'form_data':form_data
    }
    return render(request,'master/base-form.html',context)

def signout_page(request):
    logout(request)
    messages.success(request,'Logout SuccessFully')
    return redirect('login_page')
    
    
def profile_page(request):
    user_data=ProfileInfo.objects.get(user=request.user)
    context={
        'user_data':user_data
    }
    return render(request, 'profile.html',context)

def update_details(request):
    current_user=request.user
    try:
        #current_user=request.user.user_info
        user_data=ProfileInfo.objects.get(user=current_user)
    except ProfileInfo.DoesNotExist:
        user_data=None
    
    if request.method=="POST":
        form_data=UserProfileForm(request.POST,instance=user_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.user=current_user
            # For a male
            # BMR= 66.47+(13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years)
            # For a female
            # BMR=655.1+(9.563 x weight in kg)+(1.850 xheight in cm) - (4.676 x age in years)

            if data.gender=='Male':
                data.bmr=66.47+(13.75*data.weight)+(5.003*data.height)-(6.755*data.age)
            else:
                data.bmr=655.1+(9.563*data.weight)+(1.850*data.height)-(4.676*data.age)
            
            data.save()
            messages.success(request,'Profile Update SuccessFully')
            return redirect('profile_page')
    form_data=UserProfileForm(instance=user_data)
    context={
        'form_data':form_data
    }
    return render(request,'master/base-form.html',context)

def dashboard_page(request):
    
    
    return render(request,'Dashboard.html')

