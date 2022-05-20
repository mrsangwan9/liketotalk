from django.urls import path
from . import views


urlpatterns = [

    path('',views.signupp, name= 'signup'),
    path('terms/', views.terms, name = 'terms'),
    path('login/',views.loginn,name='login'),
    path('profile/', views.profile,name = 'profile'),
    path('logout',views.logoutt,name='logout'),
    path('message/<int:other_user_id>',views.messagee, name= "message")
]
