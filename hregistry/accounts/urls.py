"""accounts URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login',views.loginPage, name="loginPage"),
    path('logout',views.logOutPage, name="logoutPage"),
    path('profile',views.viewProfile,name="viewProfile"),
    path('profile/edit',views.editProfile,name="editProfile"),
    path('profile/edit/change-pass',views.changeAdminPass,name="changeAdminPass"),
    path('manage-users/',views.manageUsers, name='manageUsers'),
    path('manage-users/users/',views.users,name='users'),
    path('manage-users/edit/<int:pk>',views.editUser, name='editUser'),
    path('manage-users/edit/change-pass/<int:pk>/',views.changePass,name='changePass'),
     path('delete/<int:pk>',views.deleteUser.as_view(), name='deleteUser'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)