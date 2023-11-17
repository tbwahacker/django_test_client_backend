from rest_framework import viewsets
from base import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@permission_classes([IsAuthenticated])
class ClientViewSet (viewsets.ModelViewSet):
    queryset = models.Clients.objects.all()
    serializer_class = serializers.ClientsSerializer

    #list(),retrieve(),create(),update(),destroy()