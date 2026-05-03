from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from relational_app.models import CustomUserInfoModel,ProfileModel
from relational_app.forms import ProfileForm

# Create your views here.
# Auth User
def sign_up(request):
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        if confirm_password==password:
            CustomUserInfoModel.objects.create_user(
              full_name=full_name,
               username=username,
                email=email,
                password=password
            )
            return redirect('login_page')
            
    
    return render(request,'register.html')


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user_data=authenticate(request,username=username,password=password)
        if user_data:
            login(request,user_data)
            return redirect('home_page')

    
    return render(request,'login.html')
    
@login_required
def sign_out(request):
    logout(request)
    return redirect('login_page')
@login_required
def home_page(request):
    return render(request,'home.html')
@login_required
def profile_page(request):
    
    user_data=ProfileModel.objects.all()
    
    context={
        'user_data':user_data
    }
    
    return render(request,'profile.html',context)
@login_required
def update_profile(request):
    current_user=request.user
    try:
        profile_data=ProfileModel.objects.get(user=current_user)
    except ProfileModel.DoesNotExist:
        profile_data=None
        
    if request.method=="POST":
        form_data=ProfileForm(request.POST,request.FILES,instance=profile_data)
        if form_data.is_valid:
            data=form_data.save(commit=False)
            data.user=current_user
            data.save()
            return redirect('profile_page')
        
    
    form_data=ProfileForm(instance=profile_data)
    context={
        'form_data':form_data,
        'btn_title':'Update Profile Info',
        'btn_submit':'Update Info'
        
        
    }
    
    return render(request,'master/base-form.html',context)

# Product

def product_list(request):
    return render(request,'product-list.html')