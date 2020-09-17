from django.urls import path

from . import views


urlpatterns = [
    path('',views.home,name='home'),#home page
    path('register',views.register,name='register'), #register page
    path('login',views.login,name='login'), #login page
    path('logout',views.logout,name='logout'), #logout page
    path('profile',views.profile,name='profile'), #profile page
    path('smartphones',views.smartphones,name='smartphones'), # smartphone section
    path('laptops',views.laptops,name='laptops'), # laptop section
    path('tablets',views.tablets,name='tablets'), # tablet section
    path('mouseandkeyboard',views.mouseandkeyboard,name='mouseandkeyboard'), 
    path('headphone' ,views.headphone,name='headphone'), # headphone section
    path('hometheater' ,views.hometheater,name='hometheater'), # hometheater section
    path('addcart/<str:pk>/',views.addcart,name='addcart'), # add products
    path('viewcart',views.viewcart,name='viewcart'), # view cart 
    path('removecart/<str:pk>/',views.removecart,name='removecart'), #  removing products
    path('buy/<str:pk>/',views.buy,name='buy'),
   
]