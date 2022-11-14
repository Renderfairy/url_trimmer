from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'url_trimmer'
router = SimpleRouter()
router.register('links', views.URLViewSet, basename='links')

urlpatterns = router.urls
