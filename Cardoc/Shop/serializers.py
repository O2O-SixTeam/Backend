from rest_framework import serializers

from Shop.models import Shop


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.CustomID')

    class Meta:
        model = Shop
        fields = ('owner', 'shopname')