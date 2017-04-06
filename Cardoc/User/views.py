from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from User.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     token, created = Token.objects.get_or_create(user=serializer.instance)
    #     return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)


class DeleteToken(APIView):
    """
    POST요청이 오면 request.user가 인증되어 있는 경우, request.auth의 Token을 삭제
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)