# P2P Messaging System

A Python-based peer-to-peer messaging system with API, pub-sub, encryption, and local storage.

## Features
- Socket-based messaging
- Flask REST API
- Pub-Sub messaging
- AES encrypted messages
- Local file storage

## How to Run
1. Install requirements:
   ```bash
   pip install -r requirements.txt
python server.py
python client.py
python api.py

Project Structure
server.py: socket server

client.py: socket client

api.py: Flask API

pubsub.py: pub-sub logic

security.py: encryption module

storage.py: local JSON storage

utils.py: helper functions
