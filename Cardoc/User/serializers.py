from rest_framework import serializers

from User.models import CustomUser, Shop


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #Shop = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('name', 'phone', 'gender', 'email', 'birth', 'CustomID', 'password')


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Shop
        fields = ('shopname',)
