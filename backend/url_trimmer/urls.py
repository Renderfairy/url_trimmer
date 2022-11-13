from django.urls import path

from . import views

app_name = 'url_trimmer'

urlpatterns = [
    path('my-links/<int:link_id>/', views.link_detail_view, name='link_detail'),
    path('<str:alias>/', views.link_redirect, name='link_redirect'),
    path('my-links/<str:alias>/', views.link_delete, name='link_delete'),
    path('links-list', views.ListURLView.as_view(), name='urls_list'),
    path('add-url', views.AddURL.as_view(), name='add_url')
]
