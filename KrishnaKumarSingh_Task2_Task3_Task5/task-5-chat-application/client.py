"""
Chat Application - Client
--------------------------
Connects to the chat server and allows real-time, bidirectional
message exchange. Run two instances of this script (in separate
terminals) on the same machine to chat with yourself locally, or
have a friend on the same network connect to your IP.

Type /quit or /exit to leave the chat.

Author: <your name here>
"""

import socket
import threading

HOST = "127.0.0.1"
PORT = 5555


def receive_messages(sock: socket.socket) -> None:
    """Continuously listens for incoming messages and prints them."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\n[Disconnected from server]")
                break
            print(data.decode("utf-8"), end="")
        except OSError:
            break


def start_client(host: str = HOST, port: int = PORT) -> None:
    """Connects to the chat server and starts sending/receiving messages."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host, port))
    except (ConnectionRefusedError, OSError):
        print(f"Could not connect to server at {host}:{port}. Is the server running?")
        return

    receiver_thread = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
    receiver_thread.start()

    print("Connected! Type your messages below. Type /quit to leave.\n")

    try:
        while True:
            message = input()
            if message.strip().lower() in ("/quit", "/exit"):
                break
            sock.sendall(message.encode("utf-8"))
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        sock.close()
        print("You have disconnected. Goodbye!")


if __name__ == "__main__":
    start_client()
