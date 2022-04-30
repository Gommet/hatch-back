from rest_framework import serializers, viewsets
from caches.models import Cache
from caches.models import Submmit
from compare.utils import are_similar
from caches.serializers import SubmmitSerializer

# Create your views here.
class SubmmitViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for interacting with Enterprises
    """
    queryset = Submmit.objects.all()
    serializer_class = SubmmitSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        v = serializer.save()
        cache = Cache.objects.get(serializer.validated_data['id'])
        return Response(are_similar(serializer.validated_data['image'], cache.image))




