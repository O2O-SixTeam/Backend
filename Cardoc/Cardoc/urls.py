"""Cardoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.authtoken import views as authtoken_views
from rest_framework.routers import DefaultRouter

from Estimate import views as estimateview
from Request import views as requestview
from Shop import views as shopview
from User import views
from User.views import LogoutView

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'shop', shopview.ShopViewSet)
router.register(r'request', requestview.RequestVeiwSet)
router.register(r'estimate', estimateview.EstimateViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^token-auth/', authtoken_views.obtain_auth_token),
    url(r'^rest-auth/logout/$', LogoutView.as_view()),
    url(r'^token-delete/$', views.DeleteToken.as_view()),

]
# Authorization
# Basic Y2hhbmdqYTg4OmRqZG5sczg4
# 855403c2a6d9b7f43552ac14d7a3fa3a2e05c53c"

#855403c2a6d9b7f43552ac14d7a3fa3a2e05c53c
