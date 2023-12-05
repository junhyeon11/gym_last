
from django.urls import path
from .views import mypasesmall_view,logout_funtion

urlpatterns = [
    path("mypasesmall_view/",mypasesmall_view,name="mypasesmall_view"),
    path("logout_funtion/",logout_funtion,name="logout_funtion")
]
