from .models import Light
from rest_framework import serializers


class LightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Light
        fields = ['count']