from rest_framework import serializers
from .models import Locate


class LocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locate
        fields = '__all__'
