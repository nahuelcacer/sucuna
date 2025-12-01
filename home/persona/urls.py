from django.urls import path
from .views import PaymentInfoView, PersonaContactoView, PersonaListCreateView
urlpatterns = [
    path('personas/', PersonaListCreateView.as_view(), name='persona-list-create'),
    path('personas/<int:persona_id>/contactos/', PersonaContactoView.as_view(), name='persona-contacto'),
    path('personas/<int:persona_id>/payment-info/', PaymentInfoView.as_view(), name='persona-payment-info'),
]