# main/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_information_table

class CustomUserAdmin(UserAdmin):
    model = User_information_table

admin.site.register(User_information_table, CustomUserAdmin)
