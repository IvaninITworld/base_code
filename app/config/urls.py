from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from . import views

urlpatterns = [
    re_path("signup", views.signup),
    re_path("login", views.login),
    re_path("test_token", views.test_token),
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/doc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="doc",
    ),
    path("accounts/", include("allauth.urls")),
]
