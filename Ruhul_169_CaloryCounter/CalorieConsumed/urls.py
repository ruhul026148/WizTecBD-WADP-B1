from django.urls import path
from CalorieConsumed.views import signup_page,login_page,dashboard_page,profile_page,update_profile,calorie_consume,add_calorie,update_calorie,signout_page,delete_cosume

urlpatterns = [
    path('',signup_page,name='signup_page'),
    path('login-page/',login_page,name='login_page'),
    path('signout-page/',signout_page,name='signout_page'),
    
    
    path('profile-page/',profile_page,name='profile_page'),
    path('update-profile/',update_profile,name='update_profile'),
    
    
    path('dashboard-page/',dashboard_page,name='dashboard_page'),
    
    
    path('calorie-consume/',calorie_consume,name='calorie_consume'),
    path('add-calorie/',add_calorie,name='add_calorie'),
    path('update-calorie/<int:t_id>/',update_calorie,name='update_calorie'),
    path('delete-cosume/<int:t_id>/',delete_cosume,name='delete_cosume'),
]

