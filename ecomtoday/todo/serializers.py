from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    body = serializers.CharField()
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)