from rest_framework import serializers

from Shop.models import Shop


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.customid')
    #owner = serializers.HyperlinkedRelatedField(many=False, view_name='owner-detail', read_only=True)


    class Meta:
        model = Shop
        fields = (
            'url', 'owner', 'shopname', 'address', 'zone', 'detail', 'number', 'video', 'photo1', 'photo2', 'photo3',
            'longitude', 'latitude',)

