"""hikyaku_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from user_maintenance import urls as user_maintenance_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^user_maintenance/', include(user_maintenance_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from user_maintenance.urls import router as user_maintenance_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(user_maintenance_router.urls)),
]
