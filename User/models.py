from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)



    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    image = models.ImageField(upload_to='image',blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)  # 위치
    birth_date = models.DateField(blank=True, null=True)  # 생일
      # 프로필 사진

    def __str__(self):
        return self.bio
