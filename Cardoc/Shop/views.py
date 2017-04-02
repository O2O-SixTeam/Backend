from rest_framework import permissions
from rest_framework import viewsets

from Shop.models import Shop
from Shop.serializers import ShopSerializer
from User.permissions import IsOwnerOrReadOnly


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(owner=self.request.user)
