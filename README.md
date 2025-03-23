# P2P Messaging System

This project implements a peer-to-peer (P2P) messaging system in Python that includes socket-based communication, RESTful messaging APIs, a publish-subscribe mechanism, AES-based encryption, and local key management. It is designed as an educational example of decentralized communication without reliance on cloud-based or central servers.

## Features

- Peer-to-peer chat using Python sockets
- Asynchronous message handling via threading
- Flask-based messaging API
- Publish-subscribe messaging model
- AES encryption for secure communication
- Per-chat key management
- Local file storage (no central database)
- Modular and extensible architecture

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/p2p_messaging_system.git
   cd p2p_messaging_system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Start a Socket Server

```bash
python server.py
```

### Start a Socket Client

```bash
python client.py
```

### Start the Flask API Server

```bash
python api.py
```

### Example: Encrypt and Decrypt a Message

```bash
python security.py
```

### Example: Generate Keys per Chat Session

```bash
python keys.py
```

## REST API Endpoints

| Endpoint        | Method | Description                |
|-----------------|--------|----------------------------|
| `/send`         | POST   | Send a new message         |
| `/messages`     | GET    | Retrieve all stored messages |

Example usage with `curl`:

```bash
curl -X POST http://127.0.0.1:8000/send -H "Content-Type: application/json" -d '{"sender": "Alice", "receiver": "Bob", "content": "Hello Bob"}'
```

## Project Structure

```
p2p_messaging_system/
├── api.py           # REST API server using Flask
├── client.py        # Socket-based client for sending/receiving messages
├── keys.py          # Key generation and per-chat key management
├── keys.json        # Auto-generated key store (DO NOT EDIT MANUALLY)
├── pubsub.py        # Publish-subscribe mechanism
├── requirements.txt # Python dependencies
├── security.py      # AES encryption/decryption module
├── server.py        # Socket server handling multiple clients
├── storage.py       # Local JSON file-based message storage
├── utils.py         # Utility functions (e.g., message formatting)
└── README.md        # Project documentation
```

## Example Usage

### Encrypting Messages

```python
from keys import get_key_for_chat
from security import AESCipher

key = get_key_for_chat("alice_bob")
cipher = AESCipher(key)

encrypted = cipher.encrypt("Hello, Bob!")
print("Encrypted:", encrypted)

decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted)
```

### Pub-Sub

```python
from pubsub import PubSub, Subscriber

ps = PubSub()
bob = Subscriber("Bob")
ps.subscribe("weather", bob)
ps.publish("weather", "It will rain today.")
```

## Notes

- This system is fully decentralized: no data is stored in the cloud.
- All user data and keys are stored locally in flat files (`.json`).
- Designed for educational and experimental use only.

## License

This project is released under the MIT License.

## Author

Created by [Your Name]. Contributions welcome via pull requests.
```

