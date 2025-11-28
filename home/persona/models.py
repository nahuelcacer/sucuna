from django.db import models

card_types = (
    ('VISA', 'Visa'),
    ('Tuya', 'Tuya'),
    ('Cabal', 'Cabal'),
)
# Create your models here.
class Persona(models.Model):
    name = models.CharField(max_length=100)
    code_ib = models.CharField(max_length=50)
    state = models.BooleanField()

    def __str__(self):
        return self.name
    
class Contacto(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.persona.name} - {self.email}"
    
     
class PaymentInfo(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    card_type = models.CharField(max_length=10, choices=card_types)

    def __str__(self):
        return f"{self.persona.name} - {self.card_number[-4:]}"
    def set_card_number(self, raw_card_number):
        from home.settings import fernet
        self.card_number = fernet.encrypt(raw_card_number.encode()).decode()
    def get_card_number(self):
        from home.settings import fernet
        return fernet.decrypt(self.card_number.encode()).decode()