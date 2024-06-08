from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Given values
key = "sigensigensigenp"
iv = "sigensigensigenp"


def encrypt_password(password):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('latin1'))
    encrypted = cipher.encrypt(pad(password.encode('utf-8'), AES.block_size))
    return base64.b64encode(encrypted).decode('utf-8')


def decrypt_password(encrypted_password):
    encrypted_password_bytes = base64.b64decode(encrypted_password)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('latin1'))
    decrypted = unpad(cipher.decrypt(encrypted_password_bytes), AES.block_size)
    return decrypted.decode('utf-8')

