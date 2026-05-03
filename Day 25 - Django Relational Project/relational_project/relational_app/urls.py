from django.urls import path
from relational_app.views import (sign_up,
                                  login_page,sign_out,
                                  home_page,profile_page,
                                  update_profile,
                                  product_list)


urlpatterns = [
    #User Authentication 
    path('Register/',sign_up,name='sign_up'),
    path('',login_page,name='login_page'),
    path('sign-out/',sign_out,name='sign_out'),
    
    #Home Page
    path('home-page/',home_page,name='home_page'), 
    # User profile
    path('profile-page/',profile_page,name='profile_page'),
    path('update-profile/',update_profile,name='update_profile'),
    path('product-list/',product_list,name='product_list'),
     
]

