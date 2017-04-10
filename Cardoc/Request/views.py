import django_filters
from rest_framework import permissions
from rest_framework import viewsets

from Request.models import Request
from Request.serializers import RequestSerializer
from User.permissions import IsOwnerOrReadOnly


class RequestSearch(django_filters.rest_framework.FilterSet):
    queryset = Request.objects.get(completed=True)
    serializer_class = RequestSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    class Meta:
        model = Request
        fields = ['brand', 'broken1', 'broken2', 'broken3']


class RequestVeiwSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = RequestSearch

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            estimate_set=self.request.data.getlist('estimate')
        )
