from django.urls import path
from relational_app.views import (sign_up,
                                  login_page,sign_out,
                                  home_page,profile_page,
                                  update_profile,
                                  product_list,
                                  add_product,update_product)


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
    #Product
    
    path('product-list/',product_list,name='product_list'),
    path('add-product/',add_product,name='add_product'),
     
    path('update-product/<int:id>/',update_product,name='update_product'),
     
]

