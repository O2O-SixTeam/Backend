<<<<<<< HEAD
from rest_framework import serializers

from Shop.models import Shop
=======
from Shop.models import Shop
from rest_framework import serializers
>>>>>>> master


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
<<<<<<< HEAD
    #owner = serializers.HyperlinkedRelatedField(many=False, view_name='owner-detail', read_only=True)
=======

    # owner = serializers.HyperlinkedRelatedField(many=False, view_name='owner-detail', read_only=True)
>>>>>>> master


    class Meta:
        model = Shop
        fields = (
            'url', 'owner', 'shopname', 'address', 'zone', 'detail', 'number', 'video', 'photo1', 'photo2', 'photo3',
<<<<<<< HEAD
            'longitude', 'latitude',)

=======
            'longitude', 'latitude', 'bnumber')
>>>>>>> master
