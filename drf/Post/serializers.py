from rest_framework import serializers
from .models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ["__all__"]

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_is_liked(self, obj):
        user = self.context.get('request').user  # 요청한 유저
        if user.is_authenticated:
            return obj.likes.filter(user=user).exists()
        return False

    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["__all__"]