from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class TokenMixin:
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def initial(self, request, *args, **kwargs):
        # força autenticação antes do DRF decidir 401
        if not request.user or not request.user.is_authenticated:
            raise PermissionDenied("Authentication required.")
        super().initial(request, *args, **kwargs)