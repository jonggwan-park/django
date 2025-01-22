from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login,logout
from .serializers import RegisterSerializer,LoginSerializer,UserSerializer
from .models import CustomUser

# 유저리스트
class UserList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user_qs = CustomUser.objects.only('id', 'username', 'email')
        serializer = UserSerializer(user_qs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


# 회원가입

class RegisterAPIView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message","User registered successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# 로그인

class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request=request,user=user)
            return Response({"message":"Login successful"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# 로그아웃
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        logout(request) # Django의 세션 로그아웃 처리
        return Response({"message":"Logout successful"},status=status.HTTP_200_OK)

# 회원탈퇴

class DeleteUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request):
        user = request.user
        user.delete()
        return Response({"message":"Account deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        