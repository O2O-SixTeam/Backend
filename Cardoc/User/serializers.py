from rest_framework import serializers

from User.models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = 'name', 'phone', 'gender', 'email', 'birth', 'CustomID', 'password'

