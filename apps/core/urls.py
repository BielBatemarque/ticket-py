from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from apps.core.views import LoginView, APIRootView

urlpatterns = [
    path("", APIRootView.as_view(), name="api-root"),
    # 🔐 AUTH
    path("auth/login/", LoginView.as_view(), name="auth-login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="auth-refresh"),

    # 🧩 APPS
    # path("users/", include("apps.users.urls")),
    # path("tickets/", include("apps.tickets.urls")),
]