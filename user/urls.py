from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from user import views

# app_name='Users'
urlpatterns = [
    path('', views.home, name='home'), 

    path('logout/', views.logout_page, name='logout'),

    path('singup/', views.singup, name='singup')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)