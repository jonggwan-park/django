from django.contrib import admin
from .models import Post,Like

# Post 모델을 admin에 등록
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'likes_count', 'created_at')

    def likes_count(self, obj):
        return obj.likes.count()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')