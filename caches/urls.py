from rest_framework.routers import SimpleRouter
from django.urls import path

from caches.views import SubmmitViewSet

urlpatterns = [
    path('', SubmmitViewSet.as_view())
] 