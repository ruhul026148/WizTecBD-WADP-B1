from django.shortcuts import render,redirect
from CalorieConsumed.models import User,profileInfo,ConsumedCalorie
from django.contrib.auth import login,logout

from django.contrib import  messages

from CalorieConsumed.forms import RegistrationForm,LoginForm,ProfileForm,ConsumedForm
# Create your views here.

def signup_page(request):
    
    if request.method=="POST":
        form_data=RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Registration Successfully')
            return redirect('login_page')
            
        
    
    form_data=RegistrationForm()
    context={
        'form_data':form_data,
        'form_title':'Registration information',
        'form_btn':'Registration'
        
    }
    return render(request,'master/base-form.html',context)


def login_page(request):
    if request.method=="POST":
        form_data=LoginForm(request,request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            login(request,user)
            messages.success(request,'Login Successfully')
            return redirect('dashboard_page')
    
    
    form_data=LoginForm()
    context={
        'form_data':form_data,
        'form_title':'Login information',
        'form_btn':'Login'
    }
    return render(request,'master/base-form.html',context)


def signout_page(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return redirect('login_page')


def dashboard_page(request):
    try:
        bmr=round(request.user.auth_user.bmr,2)
        
    except:
        None
    
    context={
        'required_calorie':bmr
    }
    
    
    return render(request,'dashboard.html',context)


def profile_page(request):

    
    return render(request,'profile.html')


def update_profile(request):
    
    current_user=request.user
    
    try:
        user_data=profileInfo.objects.get(user=current_user)
    except profileInfo.DoesNotExist:
        user_data=None
        
    if request.method=="POST":
        form_data=ProfileForm(request.POST,instance=user_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.user=current_user
            weight=data.weight
            height=data.height
            age=data.age
            if data.gender=='Male':
                data.bmr=66.47+(13.75*weight)+(5.003*height)-(6.755*age)
            else:
                data.bmr=655.1+(9.567*weight)+(1.850*height)-(4.676*age)
            data.save()
            
            messages.success(request,'Login Successfully')
            return redirect('profile_page')
    
    
    
    form_data=ProfileForm(instance=user_data)
    context={
        'form_data':form_data,
        'form_title':'Update Profile Info',
        'form_btn':'Update'
    }
    
    return render(request,'master/base-form.html',context)


def calorie_consume(request):
    data=ConsumedCalorie.objects.filter(consume_by=request.user)
    context={
        'data':data
    }
    
    return render(request,'calorie-consume.html',context)


def add_calorie(request):
    if request.method=="POST":
        form_data=ConsumedForm(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.consume_by=request.user
            data.created_at
            data.save()
            messages.success(request,'Calorie Consumed Added Successfully')
            return redirect('calorie_consume')
    form_data=ConsumedForm()
    context={
        'form_data':form_data,
        'form_title':'Add Calorie Consumed Info',
        'form_btn':'Add Calorie'
    }
    return render(request,'master/base-form.html',context)



def update_calorie(request,t_id):
    current_user=request.user
    
    try:
        user_data=ConsumedCalorie.objects.get(id=t_id)
    except profileInfo.DoesNotExist:
        user_data=None
    if request.method=="POST":
        form_data=ConsumedForm(request.POST,instance=user_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.consume_by=current_user
            data.save()
            messages.success(request,'Calorie Consumed Updated Successfully')
            return redirect('calorie_consume')
    form_data=ConsumedForm(instance=user_data)
    context={
        'form_data':form_data,
        'form_title':'Update Calurie Info',
        'form_btn':'Update'
    }
    return render(request,'master/base-form.html',context)


def delete_cosume(request,t_id):
    ConsumedCalorie.objects.get(id=t_id).delete()
    messages.success(request,'Calorie Consumed Delete Successfully')
    return redirect('calorie_consume')
    
    
    