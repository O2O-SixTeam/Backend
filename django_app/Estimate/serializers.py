from rest_framework import serializers

from Estimate.models import Estimate


class EstimateSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Estimate
        fields = (
            'url', 'owner', 'targetrequest', 'noninsurancecost', 'insurancecost', 'detail', 'completed'
        )
