# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User

from user.serializers import UserSerializer

@api_view(['POST'])
def user_registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response("Login successful", status=status.HTTP_200_OK)
    return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response("Logout successful", status=status.HTTP_200_OK)

from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['POST'])
def user_password_reset(request):
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    if user:
        
        send_mail(
            title='Password Reset',  
            text='Assalomu alaykum, parolni tiklash uchun havolani quyidagi manzilga kiring: http://example.com/reset-password',  # Xabar matni
            email='from@example.com',  
            from_email=['azimovmurod126@gmail.com'],  
            fail_silently=False,
        )
        return Response("Password reset email sent", status=status.HTTP_200_OK)
    return Response("No user found with this email", status=status.HTTP_404_NOT_FOUND)
