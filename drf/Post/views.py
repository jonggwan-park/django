from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import Post,Comment,Like
from .serializers import PostSerializer,CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class PostListAPIView(APIView):
    def get(self,request):
        post_qs = Post.objects.all()
        serializer =PostSerializer(post_qs, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    def get_serializer_context(self):
        # 요청 정보를 Serializer에 전달
        return {'request': self.request}    


class PostDetailAPIView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Post,pk=pk)
    
    def get(self,request,pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self,request,pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CommentListAPIView(APIView):
    def get(self,request,post_pk):
        post = get_object_or_404(Post,pk=post_pk)
        comments= post.comments.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    
    def post(self,request,post_pk):
        post=get_object_or_404(Post,pk=post_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class CommentDetailAPIView(APIView):
    def get_object(self,comment_pk):
        return get_object_or_404(Comment,pk=comment_pk)

    def put(self,request,comment_pk):
        comment=self.get_object(comment_pk)
        serializer = CommentSerializer(comment,request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,comment_pk):
        comment=self.get_object(comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikePostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,post_pk):
        post=get_object_or_404(Post,id=post_pk)
        user = request.user
        like, created = Like.objects.get_or_create(user=user, post=post)
        if not created:
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)

        # 좋아요 추가
        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
