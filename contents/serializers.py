from rest_framework import serializers
from contents.models import Content
from rest_framework.validators import UniqueValidator


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            "id",
            "name",
            "content",
            "video_url",
        ]
        extra_kwargs = {
            "id": {
                "validators": [
                    UniqueValidator(
                        queryset=Content.objects.all(),
                        message="content not found.",
                    )
                ]
            },
        }