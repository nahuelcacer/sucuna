
from rest_framework import serializers
from .models import PaymentInfo, Persona, Contacto

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id', 'email', 'phone_number']

class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = ['id', 'card_number', 'expiration_date', 'cvv', 'card_type']
     
class PersonaSerializer(serializers.ModelSerializer):
    contactos = ContactoSerializer(many=True, read_only=True)
    payment_infos = PaymentInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Persona
        fields = ['id', 'name', 'code_ib', 'state' , 'contactos', 'payment_infos']