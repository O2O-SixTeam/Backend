from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework import viewsets
from Request.models import Request
from Request.serializers import RequestSerializer
from User.permissions import IsOwnerOrReadOnly


class RequestVeiwSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)