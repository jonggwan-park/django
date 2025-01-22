from django.urls import path
from Post import views
urlpatterns=[
    path('',views.PostListAPIView.as_view(),name='postlist'),
    path('<int:post_pk>/',views.PostDetailAPIView.as_view(),name='postdetail'),
    path(
        '<int:post_pk>/comments/',
        views.CommentListAPIView.as_view(),
        name='comment_list'
        ),
    path(
    "comments/<int:comment_pk>/",
    views.CommentDetailAPIView.as_view(),
    name="comment_detail"
    ),
    path(
        '<int:post_pk>/like/',views.LikePostAPIView.as_view(),name='like-post'),
]