from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from songs.views import SongViewSet

router = routers.DefaultRouter()
router.register(r"songs", SongViewSet, basename="songs")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
