
from rest_framework import serializers
from .models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'name', 'code_ib', 'state']


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'persona', 'email', 'phone_number']
