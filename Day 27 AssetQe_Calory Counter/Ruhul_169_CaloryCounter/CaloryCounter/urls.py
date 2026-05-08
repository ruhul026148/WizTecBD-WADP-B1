from django.urls import path
from CaloryCounter.views import (singup_page,login_page,Update_calorie,delete_calorie,
                                 dashboard_page,calorie_consume,add_calorie,
                                 signout_page,profile_page,update_details)


urlpatterns = [
    path('register/',singup_page,name='singup_page'),
    path('',login_page,name='login_page'),
    path('signout-page/',signout_page,name='signout_page'),
    
    
    
    path('profile-page/',profile_page,name='profile_page'),
    path('update-details/',update_details,name='update_details'),
    
    
    path('calorie-consume/',calorie_consume,name='calorie_consume'),
    path('add-calorie/',add_calorie,name='add_calorie'),
    path('Update-calorie/<int:id>/',Update_calorie,name='Update_calorie'),
    path('delete-calorie/<int:id>/',delete_calorie,name='delete_calorie'),
    

    
    path('dashboard-page/',dashboard_page,name='dashboard_page'),
]
