
from rest_framework import viewsets, status
from api.models import user, tweet
from api.serializers import UserSerializer, tweetSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView




class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    # @action(detail=True, methods=['get'])
    # def tweets(self, request):
    #     us = user.objects.get()
    #     tweets = tweet.objects.filter(user=us)
    #     tweet_serializer = UserSerializer(us,many = True,context={'request':request})
    #     return Response(tweet_serializer.data)


class TweetViewSet(viewsets.ModelViewSet):
    queryset = tweet.objects.all()
    serializer_class = tweetSerializer


class d_detail(APIView):

    def delete(self, request, id=None):
        us = user.objects.filter(id=id)
        us.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
