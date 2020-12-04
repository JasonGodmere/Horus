
from rest_framework import serializers



### EOH to Horus data sync serializers ###

# Performance Model
from EOH.models import Performance

class PerformanceSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()

    general_data = serializers.DictField(child=serializers.CharField(), default={})
    cpu_data = serializers.DictField(child=serializers.CharField(), default={})
    gpu_data = serializers.DictField(child=serializers.CharField(), default={})

    class Meta:
    	model = Performance

    def create(self, validated_data):
        """
        Create and return a new `Performance` entry, given the validated data.
        """
        return validated_data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.general_data = validated_data.get('general_data', instance.general_data)
        instance.cpu_data = validated_data.get('cpu_data', instance.cpu_data)
        instance.gpu_data = validated_data.get('gpu_data', instance.gpu_data)
        instance.save()
        return instance