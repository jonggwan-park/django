from django.contrib import admin
from .models import Post

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    pass