from cryptography.fernet import Fernet

# Generar una nueva key
key = Fernet.generate_key()
print(key.decode())  # para verla como string
