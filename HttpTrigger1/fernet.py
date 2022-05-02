from cryptography.fernet import Fernet

def getGenerateKey():
    key = Fernet.generate_key()
    fk = str(key)
    return fk


def encryptMsg(key, msg):
    f = Fernet(key)
    token = f.encrypt(b'msg')
    return token

def decryptMsg(key, token):
    f = Fernet(key)
    decryptToken = f.decrypt(token)
    return decryptToken

# token = f.decrypt(token)
# print(token)

# print (getGenerateKey() )