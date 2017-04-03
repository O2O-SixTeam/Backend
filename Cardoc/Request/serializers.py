from rest_framework import serializers

from Request.models import Request


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.customid')

    class Meta:
        model = Request
        fields = (
            'owner', 'brand', 'model', 'carnumber', 'broken1', 'broken2', 'broken3', 'photo1', 'photo2', 'photo3',
            'detail', 'extra', 'number'
        )
