import socket
import threading

def handle_client(conn, addr):
    print(f"[+] New connection from {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"[Received from {addr}]: {msg}")
        except:
            break
    conn.close()
    print(f"[-] Disconnected {addr}")

def start_server(host='0.0.0.0', port=5001):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[+] Server listening on {host}:{port}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    start_server()
