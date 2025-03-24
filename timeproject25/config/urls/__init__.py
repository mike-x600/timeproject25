from django.urls import include, path, re_path
from django.contrib import admin
from django.views.static import serve
from django.conf import settings


from .swagger_urls import swagger_urlpatterns
from timeproject25.apps.timeproject25.api.urls import urlpatterns as timeproject25_urlpatterns

# api_urls = [
#     # path('todos/', include('todos.urls')),
#     # path('', include('users.urls')),
#     path('', include(swagger_urlpatterns),),
# ]

admin_urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns = []
urlpatterns += admin_urlpatterns
urlpatterns += swagger_urlpatterns
urlpatterns += timeproject25_urlpatterns
urlpatterns += [
    re_path(r"^static/(?P<path>.*)$",
        serve,
        {"document_root": settings.STATIC_ROOT},
    )
]


