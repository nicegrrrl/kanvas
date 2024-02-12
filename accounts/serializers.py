from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "password", "email", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"default": False},
        }

    def create(self, validated_data: dict) -> Account:
        if validated_data["is_superuser"]:
            return Account.objects.create_superuser(**validated_data)
        return Account.objects.create_user(**validated_data)
