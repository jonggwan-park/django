from django.urls import path
from User import views
urlpatterns=[
    path('',views.UserList.as_view(),name="users"),
    path('register/',views.RegisterAPIView.as_view(),name="register"),
    path('login/',views.LoginAPIView.as_view(),name='login'),
    path('logout/',views.LogoutAPIView.as_view(),name="logout"),
    path('delete/',views.DeleteUserAPIView.as_view(),name='delete'),
]