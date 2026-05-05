from django.urls import path
from auth_formapp.views import register_page,login_page,dashboard_page,logout_page


urlpatterns = [
    path('',register_page,name='register_page'),
    path('login-page/',login_page,name='login_page'),
    path('logout-page/',logout_page,name='logout_page'),
    path('dashboard/',dashboard_page,name='dashboard_page'),
]



