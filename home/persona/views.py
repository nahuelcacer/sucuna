from django.shortcuts import render
from .models import Persona
from .serializers import ContactoSerializer, ContactoSerializer, PersonaSerializer
from rest_framework.views import APIView, Response, status  
# Create your views here.
class PersonaListCreateView(APIView):

    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PersonaContactoView(APIView):
    def get(self, request, persona_id):
        try:
            persona = Persona.objects.get(id=persona_id)
        except Persona.DoesNotExist:
            return Response({"error": "Persona not found"}, status=status.HTTP_404_NOT_FOUND)

        contactos = persona.contacto_set.all()
        serializer = ContactoSerializer(contactos, many=True)
        return Response(serializer.data)
    def post(self, request, persona_id):
        try:
            persona = Persona.objects.get(id=persona_id)
        except Persona.DoesNotExist:
            return Response({"error": "Persona not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(persona=persona)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)