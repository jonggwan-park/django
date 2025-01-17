from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignupForm
from django.contrib.auth import login,logout
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST) 
        if form.is_valid():
            user = form.save()  # User 객체 생성
            # UserProfile을 직접 생성
            UserProfile.objects.create(user=user)
            login(request,user)
            return redirect('home')
    else :
        form = SignupForm()
    return render(request,"User/signup.html",context={'form':form})

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'user/loginview.html',context={'form':form})

def profile_view(request, pk):
    profile = get_object_or_404(UserProfile,user__pk=pk)  # pk에 해당하는 사용자 프로필 가져오기
    return render(request, 'user/profile.html', {'profile': profile})

def home(request):
    return render(request, 'base.html')

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect("home")


