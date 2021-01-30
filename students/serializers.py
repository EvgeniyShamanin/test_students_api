from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    birthday = serializers.DateField()
    progress = serializers.CharField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.progress = validated_data.get('progress', instance.progress)
        instance.save()
        return instance