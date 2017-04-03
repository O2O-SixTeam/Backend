from rest_framework import serializers

from Shop.models import Shop


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.customid')

    class Meta:
        model = Shop
        fields = ('shopname', 'url', 'owner', 'address', 'detail', 'video', 'number', 'longitude', 'latitude', 'zone')
