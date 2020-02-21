from rest_framework import serializers
from .models import operation

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = operation
        fields = '__all__'