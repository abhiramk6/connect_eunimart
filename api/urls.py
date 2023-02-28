from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import UserViewSet,TweetViewSet


router=routers.DefaultRouter()
router.register(r'user',UserViewSet)
router.register(r'tweet',TweetViewSet)

urlpatterns = [

    path('', include(router.urls))
]

