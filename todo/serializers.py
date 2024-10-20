from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.IntegerField(), required=True, write_only=True
    )
    completed = serializers.BooleanField(default=False)

    def validate_tags(self, value):
        tags = Tag.objects.filter(id__in=value).count()
        if tags != len(value):
            raise serializers.ValidationError("Invalid tag id")
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["tags"] = TagSerializer(instance.tags.all(), many=True).data
        return data

    class Meta:
        model = Task
        fields = "__all__"
