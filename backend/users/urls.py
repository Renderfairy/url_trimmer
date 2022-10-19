from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.login_user_view, name='login'),
    path('register', views.registration_view, name='register'),
]
