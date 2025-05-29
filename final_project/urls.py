"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from django.urls import path
from django.contrib.auth import views as au
from django.urls import path, include
from .views import custom_login, register, custom_logout, home_view
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    #path ('', home_view, name='home'),
    path ('', views.recipe_list, name='home'),
    path ('login/', custom_login, name='login'),
    path ('register/', register, name='register'),
    path ('logout/', custom_logout, name='logout'),
    path('', views.recipe_list, name='recipe_list'),
    path('chronos', views.chronos, name='chronos' ),
    path('create/', views.recipe_create, name='recipe_create'),
    path('<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),


    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('', home_view, name='home'),
]

# use default Django views for:
# Login (LoginView)
# Logout (LogoutView)
# Password Change / Reset
# wire/link them in here


