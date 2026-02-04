from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.reverse import reverse
from apps.core.mixins import TokenMixin
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, MeSerializer

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

class MeView(TokenMixin, ModelViewSet):
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user