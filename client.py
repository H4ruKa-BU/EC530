import socket
import threading

def receive_messages(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg:
                print(f"\n[New Message]: {msg}")
        except:
            print("[-] Connection closed")
            break

def start_client(server_ip='127.0.0.1', server_port=5001):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    print("[+] Connected to server")

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        client.send(msg.encode('utf-8'))

    client.close()

if __name__ == '__main__':
    start_client()
