from django.urls import include, path
from . import views


urlpatterns = [
    path(f"minimal/", views.minimal_view, name='minimal_view')
]