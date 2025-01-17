from django.shortcuts import render,redirect
from .models import Post
from django.views.decorators.http import require_POST
from .forms import PostForm
from django.shortcuts import get_object_or_404
from User.models import CustomUser

def post_list(request):
    posts = Post.objects.all()
    return render(request,'post/post_list.html',context={'posts': posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 저장하기 전 추가 데이터 설정
            post.author = request.user  # 작성자 설정
            post.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, 'post/post_create.html', context={'form': form})

    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Post/post_detail.html', {'post': post})

@require_POST
def post_delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.pk == post.author.pk:
        post.delete()       
        return redirect("home")
    else:
        return redirect('loginview')
    
def post_update(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user.pk != post.author.pk:
        return redirect('post_list') 
    
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail',pk=post.pk)
    else :
        form = PostForm(instance=post)
    
    return render(request, 'post/post_update.html', {'form': form, 'post': post})
    
