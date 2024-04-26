# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('password/reset/', views.user_password_reset, name='user_password_reset'),
]
