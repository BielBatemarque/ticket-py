from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.reverse import reverse
from apps.core.mixins import TokenMixin
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, MeSerializer, LogutSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response({
            "auth": {
                "login": reverse("auth-login", request=request, format=format),
                "refresh": reverse("auth-refresh", request=request, format=format),
            },
            "me": reverse("me", request=request, format=format)
            # "users": reverse("users-root", request=request, format=format),
        })
    
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LogoutView(TokenMixin, ModelViewSet):
    serializer_class = LogutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refrest_token = RefreshToken(serializer.validated_data.get("refresh_token"))
        refrest_token.blacklist()

        return Response({"detail": "Logout realizado com sucesso"}, status=status.HTTP_205_RESET_CONTENT)

class MeView(TokenMixin, ModelViewSet):
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user
    