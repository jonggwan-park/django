from django.contrib import admin
from .models import CustomUser,UserProfile

@admin.register(CustomUser)
class CustomUseradmin(admin.ModelAdmin):
    pass

@admin.register(UserProfile)
class UserProfileadmin(admin.ModelAdmin):
    pass