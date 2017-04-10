import django_filters
from rest_framework import permissions
from rest_framework import viewsets

from Shop.models import Shop
from Shop.serializers import ShopSerializer
from User.permissions import IsOwnerOrReadOnly


# http://127.0.0.1:8000/shop?zone=apt1 URL 형식
class ShopSearch(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Shop
        fields = ['zone']


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ShopSearch

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(owner=self.request.user)
