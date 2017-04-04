from rest_framework import serializers

from Estimate.models import Estimate
from Estimate.serializers import EstimateSerializer
from Request.models import Request


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    requestedby = serializers.ReadOnlyField(source='owner.customid')
    #estimate = serializers.HyperlinkedRelatedField(many=True, view_name='request-detail',read_only=True)

    estimate = EstimateSerializer(many=True, source='estimate_set', read_only=True)

    class Meta:
        model = Request
        fields = (
            'url', 'requestedby', 'brand', 'model', 'carnumber', 'broken1', 'broken2', 'broken3', 'photo1', 'photo2',
            'photo3', 'detail', 'extra', 'number', 'completed', 'estimate'
        )

    # def create(self, validated_data):
    #     estimates = validated_data.pop('estimate_set')
    #     estimate = Estimate.objects.create(**validated_data)
    #     for estimate in estimates:
    #         Estimate.objects.create(
    #             **validated_data
    #
    #
    #         )
    #     return estimate