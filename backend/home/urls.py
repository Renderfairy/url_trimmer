from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("home-2", views.HomeView.as_view(), name="home_2")
]
