from django.urls import path
from ManageCash.views import (signup_page,login_page,
                              dashboard_page,signout_page,profile_page,
                              cash_list,addcash_page,updatecash_page,delete_cash,
                              addexpnese_page,expense_list,updateexpnese_page,delete_expense)

urlpatterns = [
    path('signup-page/',signup_page,name='signup_page'),
    path('',login_page,name='login_page'),
    path('signout-page/',signout_page,name='signout_page'),
    
    
    path('profile-page/',profile_page,name='profile_page'),
    
    #Add Cash urls
    path('cash-list/',cash_list,name='cash_list'),
    path('addcash-page/',addcash_page,name='addcash_page'),
    path('updatecash-page/<int:id>/',updatecash_page,name='updatecash_page'),
    path('delete-expense/<int:id>/',delete_expense,name='delete_expense'),
    
    #Expenses
    path('expense-list/',expense_list,name='expense_list'),
    path('addexpnese-page/',addexpnese_page,name='addexpnese_page'),
    path('updateexpnese-page/<int:id>/',updateexpnese_page,name='updateexpnese_page'),
    path('delete-cash/<int:id>/',delete_cash,name='delete_cash'),
    
    
    
    
    path('dashboard-page/',dashboard_page,name='dashboard_page'),
]
