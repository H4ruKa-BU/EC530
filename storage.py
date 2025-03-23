import json
import os

def save_message(filename, message):
    with open(filename, 'a') as f:
        f.write(json.dumps(message) + '\n')

def load_messages(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return [json.loads(line) for line in f]

# Example usage
if __name__ == '__main__':
    save_message('chat.json', {'sender': 'Alice', 'text': 'Hello'})
    print(load_messages('chat.json'))
