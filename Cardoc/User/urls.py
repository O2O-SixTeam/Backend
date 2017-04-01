from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from User import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
