from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)
print('Clave \n' + str(key) + '\n')

token = f.encrypt(b"Mensaje que se va a encriptar")
print(token)

decryptToken = f.decrypt(token)
print(decryptToken)
print(token)

token = f.decrypt(token)
print(token)
