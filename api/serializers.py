from rest_framework import serializers
from api.models import user,tweet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #user_id = serializers.ReadOnlyField()
    class Meta:
        model = user
        fields = "__all__"

class tweetSerializer(serializers.HyperlinkedModelSerializer):
   # user_id = serializers.ReadOnlyField()
    class Meta:
        model = tweet
        fields = "__all__"

