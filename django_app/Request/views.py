import django_filters
from rest_framework import permissions
from rest_framework import viewsets

from Request.models import Request, BROKEN_CHOICE
from Request.serializers import RequestSerializer
from User.permissions import IsOwnerOrReadOnly


class RequestSearch(django_filters.rest_framework.FilterSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    broken1 = django_filters.ChoiceFilter(choices=BROKEN_CHOICE)
    broken2 = django_filters.ChoiceFilter(choices=BROKEN_CHOICE)
    broken3 = django_filters.ChoiceFilter(choices=BROKEN_CHOICE)

    class Meta:
        model = Request
        fields = {
            'brand': ['exact'],
            'broken1': ['exact'],
            'broken2': ['exact'],
            'broken3': ['exact'],
            'completed': ['exact'],
        }


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
