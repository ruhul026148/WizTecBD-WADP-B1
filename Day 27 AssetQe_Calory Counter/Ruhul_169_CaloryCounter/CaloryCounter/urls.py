from django.urls import path
from CaloryCounter.views import singup_page,login_page,dashboard_page,signout_page,profile_page,update_details


urlpatterns = [
    path('register/',singup_page,name='singup_page'),
    path('',login_page,name='login_page'),
    path('signout-page/',signout_page,name='signout_page'),
    
    
    
    path('profile-page/',profile_page,name='profile_page'),
    path('update-details/',update_details,name='update_details'),
    

    
    path('dashboard-page/',dashboard_page,name='dashboard_page'),
]
