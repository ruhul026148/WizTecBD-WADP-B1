from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from datetime import date
from django.db.models import Sum,Count

from CaloryCounter.models import User,ProfileInfo,CalorieModel

from CaloryCounter.forms import RegistrationForm,LoginForm,UserProfileForm,CalorieForm

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
    current_user=request.user
    try:
        bmr=round(current_user.user_info.bmr,2)
        
        
    except:
        bmr=0
    
    today=date.today()
    today_calorie_consume=CalorieModel.objects.filter(consumed_by=current_user,
                                                      created_at=today
                )
    
    total_calorie_consume=today_calorie_consume.aggregate(total=Sum('Calorie_consumed'),
                                                          total_count=Count('Calorie_consumed'))
    
    less_more=bmr-total_calorie_consume['total']
    
    if bmr>total_calorie_consume['total']:
        suggestion='Doya kore bisi kore khaw, nahole chikna hye jaba'
    else:
        suggestion='kom kha beta, nahole fole java'
    
    context={
        'requeid_calorie':bmr,
        'today_consumed_data':today_calorie_consume,
        'Consume_calorie':total_calorie_consume['total'],
        'total_count':total_calorie_consume['total_count'],
        'less_more':less_more,
        'suggestion':suggestion
        
    }
        
    
    return render(request,'Dashboard.html',context)

def calorie_consume(request):
    user_data = CalorieModel.objects.filter(consumed_by=request.user)

    context = {
        'user_data': user_data
    }

    return render(request, 'calorie-consume.html', context)
def add_calorie(request):
    if request.method=="POST":
        form_data=CalorieForm(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.consumed_by=request.user
            data.created_at
            data.save()
            messages.success(request,'Calorie Added SuccessFully')
            return redirect('calorie_consume')
    form_data=CalorieForm()
    context={
        'form_data':form_data
    }
    return render(request,'master/base-form.html',context)

def Update_calorie(request,id):
    try:
        user_data = CalorieModel.objects.get(id=id)
    except CalorieModel.DoesNotExist:
        user_data=None

    if request.method=="POST":
        form_data=CalorieForm(request.POST,instance=user_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.consumed_by=request.user
            data.created_at
            data.save()
            messages.success(request,'Calorie Update SuccessFully')
            return redirect('calorie_consume')
    form_data=CalorieForm(instance=user_data)
    context={
        'form_data':form_data
    }
    return render(request,'master/base-form.html',context)

def delete_calorie(request,id):
    CalorieModel.objects.get(id=id).delete()
    messages.success(request,'Calorie Delete SuccessFully')
    return redirect('calorie_consume')
    

