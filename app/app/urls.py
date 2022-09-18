"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from app.views import index_view, pdf_upload_view, pdf_upload, dashboard_view, dashboard_API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('pdf-upload-view', pdf_upload_view),
    path('pdf-upload', pdf_upload),
    path('api/user/', include('user.urls')),
    path("dashboard-view", dashboard_view),
    path("dashboard-data", dashboard_API),
]
