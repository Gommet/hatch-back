from rest_framework.routers import SimpleRouter
from django.urls import path

from caches.views import SubmmitViewSet

router = SimpleRouter()
router.register("", SubmmitViewSet)
urlpatterns = [] + router.urls