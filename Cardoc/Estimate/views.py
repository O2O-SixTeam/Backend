import django_filters
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets

from Estimate.models import Estimate
from Estimate.serializers import EstimateSerializer
from User.permissions import IsOwnerOrReadOnly


class EstimateSearch(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Estimate
        fields = ['completed','owner','insurancecost']


class EstimateViewSet(viewsets.ModelViewSet):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = EstimateSearch

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(owner=self.request.user)