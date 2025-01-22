from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser

# Post 모델을 admin에 등록
admin.site.register(CustomUser)