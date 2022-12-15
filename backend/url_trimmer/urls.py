from django.urls import path

from . import views

app_name = 'url_trimmer'

urlpatterns = [
    path('my-links/<int:pk>', views.LinkDetailView.as_view(), name='link_detail'),
    path('<str:alias>', views.link_redirect, name='link_redirect'),
    path('my-links/<str:alias>/delete', views.LinkDeleteView.as_view(), name='link_delete'),
]
