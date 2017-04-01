from django.conf.urls import url, include
from rest_framework.authtoken import views
from User import views

urlpatterns = [
    url(r'^create/$', views.UserCreate.as_view()),

]
