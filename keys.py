import os
import base64
import json

KEYS_FILE = 'keys.json'

def generate_key():
    return base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')

def load_keys():
    if not os.path.exists(KEYS_FILE):
        return {}
    with open(KEYS_FILE, 'r') as f:
        return json.load(f)

def save_keys(keys):
    with open(KEYS_FILE, 'w') as f:
        json.dump(keys, f, indent=2)

def get_key_for_chat(chat_id):
    keys = load_keys()
    if chat_id not in keys:
        keys[chat_id] = generate_key()
        save_keys(keys)
    return keys[chat_id]

# Example usage
if __name__ == '__main__':
    key1 = get_key_for_chat("alice_bob")
    key2 = get_key_for_chat("bob_charlie")
    print("alice_bob key:", key1)
    print("bob_charlie key:", key2)
