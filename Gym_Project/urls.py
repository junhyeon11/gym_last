"""
URL configuration for Gym_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include,path
from main.views import mainpase,mypasesmall_view
from login.views import loginpase, registerpase
urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", mainpase, name="main"),
    path("main/", include('main.urls')),
    path("login/", loginpase, name="login"),
    path("register/", registerpase, name="register"),
]