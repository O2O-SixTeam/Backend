from rest_framework import serializers

from User.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    shop = serializers.HyperlinkedRelatedField(many=True, view_name='shop-detail', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('url', 'name', 'phone', 'gender', 'email', 'birth', 'customid', 'password', 'shop')

    def create(self, validated_data):
        instance = CustomUser.objects.create_user(**validated_data)
        return instance
