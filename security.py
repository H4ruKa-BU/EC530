from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

class AESCipher:
    def __init__(self, key):
        self.key = key.encode('utf-8').ljust(32)[:32]

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
        return base64.b64encode(cipher.nonce + ciphertext).decode('utf-8')

    def decrypt(self, encrypted):
        data = base64.b64decode(encrypted)
        nonce = data[:16]
        ciphertext = data[16:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt(ciphertext).decode('utf-8')

# Example usage
if __name__ == '__main__':
    cipher = AESCipher('supersecretkey')
    encrypted = cipher.encrypt('Hello Secure World!')
    print("Encrypted:", encrypted)
    print("Decrypted:", cipher.decrypt(encrypted))
