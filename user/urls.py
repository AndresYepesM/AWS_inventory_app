from django.urls import path, include, re_path
from user import views

# app_name='Users'
urlpatterns = [
    path('', views.home, name='home'), 

    path('logout/', views.logout_page, name='logout'),

    path('singup/', views.singup, name='singup')
]