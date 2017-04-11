import django_filters
from rest_framework import permissions
from rest_framework import viewsets

from Estimate.models import Estimate
from Estimate.serializers import EstimateSerializer
from Request.models import Request
from User.permissions import IsOwnerOrReadOnly


class EstimateSearch(django_filters.rest_framework.FilterSet):
    queryset = Request.objects.filter(completed=True)

    class Meta:
        model = Estimate
        fields = {
            'owner': ['exact'],
            'noninsurancecost': ['exact']
        }


class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = EstimateSearch

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(owner=self.request.user)
