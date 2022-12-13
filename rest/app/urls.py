from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SnippetViewSet, UserViewSet

router = DefaultRouter()
router.register('snippets', SnippetViewSet, basename="snippet")
router.register('users', UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
]
