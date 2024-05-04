from rest_framework.response import Response
from account import models
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterUser(APIView):
    # authentication_classes = [IsAuthenticated]
    def post(self, request,*args, **kwargs):
        post_data = request.data
        email = post_data.get("email")
        password = post_data.get("password")
        name=post_data.get("name")

        if not email or not password or not name: 
            return Response({"error": "Email, name and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user,created = models.CustomUser.objects.get_or_create(email =email)
        if not created:
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user.name = name
        user.set_password(password)
        user.save()

        token = get_tokens_for_user(user)

        return Response({"success": "user created",
                         "token": token}, status=status.HTTP_201_CREATED)
    


class LoginUser(APIView):
    def post(self, request, *args, **kwargs):
        post_data = request.data
        email = post_data.get("email")
        password = post_data.get("password")
        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        # user = models.CustomUser.objects.filter(email=email).first()
        user = authenticate(email=email, password=password)
        if user is None:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
        
        token = get_tokens_for_user(user)
        return Response({"success": "user logged in",
                         "token": token}, status=status.HTTP_200_OK)




class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return Response(data={"success": "user logged in"}, status=status.HTTP_200_OK)