from django.conf import settings
from django.urls import path, re_path

from rest_framework.permissions import AllowAny
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

swagger_urlpatterns = [
    path("api/schema/",
         SpectacularAPIView.as_view(),
         name="schema"),
    path("swagger/",
         SpectacularSwaggerView.as_view(url_name="schema"), 
         name="swagger-ui"),
]