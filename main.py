from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)
print('Clave \n' + str(key) + '\n')
m = 'hola'
# msg = bytes(m, encoding='utf-8')
msg = m.encode()

token = f.encrypt(msg)
print(token)

decryptToken = f.decrypt(token)
print(decryptToken)
# print(token)

# token = f.decrypt(token)
# print(token)
