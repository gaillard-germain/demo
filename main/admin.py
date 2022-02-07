from django.contrib import admin

from .models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
