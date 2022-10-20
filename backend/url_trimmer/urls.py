from django.urls import path

from . import views

app_name = 'url_trimmer'

urlpatterns = [
    path('my-links/<int:link_id>', views.link_detail_view, name='link_detail')
]
