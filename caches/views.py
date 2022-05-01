from rest_framework import serializers, viewsets
from caches.models import Cache
from caches.models import Submmit
from compare.utils import are_similar
from caches.serializers import SubmmitSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from hatch.settings import MEDIA_ROOT

# Create your views here.
class SubmmitViewSet(APIView):
    """
    Submmit Cache
    """

    def post(self, request, *args, **kwargs):
        serializer = SubmmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        v = serializer.save()
        cache = Cache.objects.get(id=serializer.validated_data['cache'].id)
        print(MEDIA_ROOT+cache.image.name)
        print(MEDIA_ROOT+serializer.validated_data['image'].__str__())
        return Response(are_similar(MEDIA_ROOT+serializer.validated_data['image'].__str__(), MEDIA_ROOT+cache.image.name))




