from rest_framework import serializers

from . import models


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = [
            "last_updated",
            "created",
            "email",
        ]
