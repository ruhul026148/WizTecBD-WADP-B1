from django.shortcuts import render,redirect
from ManageCash.models import User,AddCash,Expense
from django.contrib.auth import login,logout
from ManageCash.forms import SingupForm,LoginForm,AddCashForm,ExpenseForm
from django.contrib import messages
from django.db.models import Sum

from datetime import date
from django.utils import timezone


# Create your views here.

def signup_page(request):
    if request.method=="POST":
        form_data=SingupForm(request.POST)
        if form_data.is_valid(): 
            form_data.save()
            messages.success(request,'Registration Successfully')
            return redirect('login_page')
        
    form_data=SingupForm()
    context={
       'form_data':form_data,
       'form_title':'User Registration',
       'form_btn':'Register'
    }
    
    return render(request,'master/base-form.html',context)


def login_page(request):
    if request.method=="POST":
        form_data=LoginForm(request,request.POST)
        if form_data.is_valid():
            data=form_data.get_user()
            login(request,data)
            messages.success(request,'Login Successfully')
            return redirect('dashboard_page')
    form_data=LoginForm()
    context={
       'form_data':form_data,
       'form_title':'User Login',
       'form_btn':'login'
    }
    
    return render(request,'master/base-form.html',context)

def signout_page(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return redirect('login_page')
   
def cash_list(request):
    cash_data=AddCash.objects.filter(user=request.user)
    context={
       'cash_data':cash_data
    }
    return render(request,'Cash.html',context)   
    
def addcash_page(request):
    current_user=request.user
    if request.method=="POST":
        form_data=AddCashForm(request.POST)
        if form_data.is_valid(): 
            data=form_data.save(commit=False)
            data.user=current_user
            data.save()
            messages.success(request,'Add Cash Successfully')
            return redirect('cash_list')
    form_data=AddCashForm()
    context={
       'form_data':form_data,
       'form_title':'Add Cash Data ',
       'form_btn':'Add'
    }
    
    return render(request,'master/base-form.html',context)

def updatecash_page(request,id):
    current_user=request.user
    try:
        cash_data=AddCash.objects.get(id=id)
    except AddCash.DoesNotExist:
        cash_data=None
    if request.method=="POST":
        form_data=AddCashForm(request.POST,instance=cash_data)
        if form_data.is_valid(): 
            data=form_data.save(commit=False)
            data.user=current_user
            data.save()
            messages.success(request,'Update Cash Successfully')
            return redirect('cash_list')
    form_data=AddCashForm(instance=cash_data)
    context={
       'form_data':form_data,
       'form_title':'Update Cash Data ',
       'form_btn':'Update'
    }
    
    return render(request,'master/base-form.html',context)

def delete_cash(request,id):
    AddCash.objects.get(id=id).delete()
    messages.success(request,'Cash Delete Successfully')
    return redirect('cash_list')
    




def expense_list(request):
    expense_data=Expense.objects.filter(user=request.user)
    context={
       'expense_data':expense_data
    }
    return render(request,'expense.html',context)   
    
def addexpnese_page(request):
    current_user=request.user
    if request.method=="POST":
        form_data=ExpenseForm(request.POST)
        if form_data.is_valid(): 
            data=form_data.save(commit=False)
            data.user=current_user
            data.save()
            messages.success(request,'Add Expense Successfully')
            return redirect('expense_list')
    form_data=ExpenseForm()
    context={
       'form_data':form_data,
       'form_title':'Add Expense Data ',
       'form_btn':'Add'
    }
    
    return render(request,'master/base-form.html',context)


def updateexpnese_page(request,id):
    current_user=request.user
    try:
        expense_data=Expense.objects.get(id=id)
    except Expense.DoesNotExist:
        expense_data=None
    if request.method=="POST":
        form_data=ExpenseForm(request.POST,instance=expense_data)
        if form_data.is_valid(): 
            data=form_data.save(commit=False)
            data.user=current_user
            data.save()
            messages.success(request,'Update Cash Successfully')
            return redirect('expense_list')
    form_data=ExpenseForm(instance=expense_data)
    context={
       'form_data':form_data,
       'form_title':'Update Expense Data ',
       'form_btn':'Update'
    }
    
    return render(request,'master/base-form.html',context)

def delete_expense(request,id):
    Expense.objects.get(id=id).delete()
    messages.success(request,'Cash Delete Successfully')
    return redirect('expense_list')

def dashboard_page(request):
    current_user=request.user
  
    total_Expense=Expense.objects.filter(user=current_user).aggregate(total=Sum('amount'))
    expense=total_Expense['total'] or 0
    total_Cash=AddCash.objects.filter(user=current_user).aggregate(total=Sum('amount'))
    Cash =total_Cash['total'] or 0
    less_more=Cash-expense
    
    if Cash>expense:
        messages.success(request,f'Total Saving {less_more} tk. So You are Rich')
    else:
        messages.success(request,f'Total Saving {less_more} tk. So you are poor')
        
        
  
   
        
        
    
    context={
        'total_Expense':expense,
        'total_Cash':Cash,
        'less_more':less_more,
    }
    
    
    return render(request,'dashboard.html',context)


def profile_page(request):
    current_user=request.user
    
    now=timezone.now()
    total_Cash=AddCash.objects.filter(user=current_user,datetime__month=now.month).aggregate(total=Sum('amount'))
    Cash =total_Cash['total'] or 0
    context={
        'total_Cash':Cash,
    }
    
    return render(request,'profile.html',context)
    
    
