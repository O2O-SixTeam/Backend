from rest_framework import serializers

from User.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    shop = serializers.HyperlinkedRelatedField(many=True, view_name='shop-detail', read_only=True)
    request = serializers.HyperlinkedRelatedField(many=True, view_name='request-detail', read_only=True)
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request', blank=False)
    # view_name -> related_name + -detail 써야 된다

    class Meta:
        model = CustomUser
        fields = ('url', 'name', 'phone', 'gender', 'email', 'birth', 'customid', 'password', 'shop', 'request',)

    def create(self, validated_data):
        instance = CustomUser.objects.create_user(**validated_data)
        return instance
