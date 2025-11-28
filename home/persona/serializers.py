
from rest_framework import serializers
from .models import Persona, Contacto

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id', 'email', 'phone_number']

class PersonaSerializer(serializers.ModelSerializer):
    contactos = ContactoSerializer(many=True, read_only=True)

    class Meta:
        model = Persona
        fields = ['id', 'name', 'code_ib', 'state' , 'contactos']


