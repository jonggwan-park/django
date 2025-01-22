from django.db import models
# 테이블 생성할때 상속해주는 모델을 가져온다.
from django.conf import settings
# 이 프로젝트 장고의 셋팅즈를 가져온다 이때 프로젝트 디렉토리에 있는 셋팅즈는 덮어쓰게 된다

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='posts')
    # ForeignKey로 1대 다 관계 형성 ForeignKey를 적는 쪽이 '다'
    #이므로 1명의 유저에 여러개의 포스트를 생성할 수 있다는 것임
    # 추가로 user가 삭제되었을 시 post도 삭제됨.
    title = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

# print했을 시 나오는 것
    def __str__(self):
        return self.message

# 태그라는 테이블을 생성하고 name이라는 컬럼을 만들어줌
class Tag(models.Model):
    name = models.CharField(max_length=44)

    def __str__(self):
        return self.name

class Comment(models.Model):
    pass
