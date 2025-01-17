from . import views
from django.urls import path
urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('post_create/',views.post_create,name='post_create'),
    path('post_detail/<int:pk>/',views.post_detail,name='post_detail'),
    path('post_detail/<int:pk>/post_delete/',views.post_delete,name="post_delete"),
    path('post_detail/<int:pk>/post_update/',views.post_update,name='post_update')
]