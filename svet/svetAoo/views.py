from .models import Light
from rest_framework import viewsets
from svetAoo.serializers import LightSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class LightViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = LightSerializer

    queryset = Light.objects.all()