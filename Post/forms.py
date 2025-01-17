from django import forms

from Post.models import Post

'''
Forms
1. HTML 폼을 자동 생성
2. 사용자가 입력한 데이터를 검증 -> 데이터베이스 상호 작용(반영, 저장, 쓰고, 수정하거나 등등)
'''

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','message', 'tag_set']

