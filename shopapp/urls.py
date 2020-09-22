from django.urls import path

from . import views


urlpatterns = [
    path('',views.home,name='home'),#home page
    path('register',views.register,name='register'), #register page
    path('login',views.login,name='login'), #login page
    path('logout',views.logout,name='logout'), #logout page
    path('profile',views.profile,name='profile'), #profile page

 


    path('<int:pk>', views.products,name='products'),

    path('addcart/<str:pk>/',views.addcart,name='addcart'), # add products
    path('viewcart',views.viewcart,name='viewcart'), # view cart 
    path('removecart/<str:pk>/',views.removecart,name='removecart'), #  removing products
    path('buy/<str:pk>/',views.buy,name='buy'),
   
]