"""patients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views

from django.conf.urls.static import static
from django.conf import settings
from accounts.views import *

urlpatterns = [
    path('records', views.records, name="records"),
    path('export-to-csv', views.exportToCSV, name="export_to_csv"),
    path('',views.indexPage, name="indexPage"),
    path('records/<int:year>', views.records, name="records"),
    path('records/edit/<str:id>',views.editRecordPage,name="editRecord"),
    path('records/delete/<str:id>', views.removeRecord, name="removeRecord"),
    path('download-records/',views.exportToCSV,name="exportToCSV"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)