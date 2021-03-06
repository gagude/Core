from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tickets, Ligacoes

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TicketsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'
        
class LigacoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ligacoes
        fields = '__all__'