from rest_framework.serializers import ModelSerializer
from base.models import Note,Clients

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class ClientsSerializer(ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__' 