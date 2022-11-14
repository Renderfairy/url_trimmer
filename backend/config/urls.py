"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import settings
from url_trimmer import views as ut_views
from users import views as u_views


router = routers.SimpleRouter()
router.register(r'users', u_views.UsersList, basename='user_list')
# router.register('links/', ut_views.ListURLView, basename='urls_list')


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("home.urls")),
    path("", include("users.urls")),
    path("", include("url_trimmer.urls")),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace='rest_framework')),

]

handler404 = ut_views.error_404

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
