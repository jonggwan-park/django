from django.db import models
from drf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimestampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="post")
    title = models.CharField(max_length=30)
    message = models.TextField()
    tag_set = models.ManyToManyField('Tag',blank=True)
    
    def __str__(self):
        return self.title
    def likes_count(self):
        return self.liked_users.count()
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user','post')
    
    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"


class Tag(TimestampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Comment(TimestampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="comment")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment")
    comment = models.TextField(max_length=50)

