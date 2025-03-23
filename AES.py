from keys import get_key_for_chat
from security import AESCipher

chat_id = 'alice_bob'
key = get_key_for_chat(chat_id)
cipher = AESCipher(key)

encrypted = cipher.encrypt("Hi Bob!")
decrypted = cipher.decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
