from rest_framework import serializers

from Estimate.models import Estimate


class EstimateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estimate
        fields = (
            'url', 'owner', 'targetrequest', 'noninsurancecost', 'insurancecost', 'detail', 'completed'
        )

        # def create(self, validated_data):
        #     instance = Estimate.objects.create_user(**validated_data)
        #     return instance
