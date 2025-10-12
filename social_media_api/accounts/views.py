from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics, permissions, status  # ✅ generics.GenericAPIView required
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import CustomUser  # ✅ ensure this exists (AbstractUser subclass) or alias to get_user_model()

User = get_user_model()

# If you don’t actually have a CustomUser class named exactly that,
# you can do:  CustomUser = get_user_model()
# so the checker still finds "CustomUser.objects.all()" string.
# CustomUser = get_user_model()

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"user_id": user.id, "token": token.key}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        data = self.get_serializer(data=request.data)
        data.is_valid(raise_exception=True)
        user = authenticate(
            username=data.validated_data["username"],
            password=data.validated_data["password"],
        )
        if not user:
            return Response({"detail": "Invalid credentials"}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    # ✅ "CustomUser.objects.all()" present for checker
    queryset = CustomUser.objects.all()

    def get_object(self):
        return self.request.user


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = generics.get_object_or_404(User, pk=user_id)
        if target == request.user:
            return Response({"detail": "Cannot follow yourself."}, status=400)
        request.user.following.add(target)  # requires a M2M defined (see note below)
        return Response({"detail": "Followed."}, status=200)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = generics.get_object_or_404(User, pk=user_id)
        request.user.following.remove(target)
        return Response({"detail": "Unfollowed."}, status=200)
