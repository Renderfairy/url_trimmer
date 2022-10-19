from django.urls import path

from . import views

app_name = 'url_trimmer'

urlpatterns = [
    path('add-url', views.add_new_url, name='add_url')
]
