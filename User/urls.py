from django import views
from django.urls import path
from User import views
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('loginview/',views.loginview,name='loginview'),
    path('profile/<int:pk>/',views.profile_view,name="profile"),
     path('logout/', LogoutView.as_view(next_page='loginview'), name='logout'),  # 로그아웃 후 리다이렉트
     path("delete/",views.delete,name="delete")
]