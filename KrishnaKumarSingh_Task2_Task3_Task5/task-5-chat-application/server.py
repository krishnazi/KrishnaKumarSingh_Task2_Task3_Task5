"""
Chat Application - Server
--------------------------
Listens for incoming client connections and relays messages between
connected clients in real time. Supports any number of clients, though
this task targets two-user chat on localhost.

Author: <your name here>
"""

import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

# Maps each connected client socket -> username
clients = {}
clients_lock = threading.Lock()


def timestamp() -> str:
    """Returns the current time formatted as HH:MM."""
    return datetime.now().strftime("%H:%M")


def broadcast(message: str, exclude_socket: socket.socket = None) -> None:
    """Sends a message to all connected clients except the excluded one."""
    with clients_lock:
        recipients = [s for s in clients if s is not exclude_socket]

    for client_socket in recipients:
        try:
            client_socket.sendall(message.encode("utf-8"))
        except OSError:
            # If sending fails, the client will be cleaned up by its own
            # handler thread when its recv() call fails.
            pass


def remove_client(client_socket: socket.socket) -> str:
    """Removes a client from the registry and closes its socket. Returns username."""
    with clients_lock:
        username = clients.pop(client_socket, None)

    try:
        client_socket.close()
    except OSError:
        pass

    return username


def handle_client(client_socket: socket.socket, address) -> None:
    """Handles the full lifecycle of a single client connection."""
    username = None
    try:
        client_socket.sendall("Enter your username: ".encode("utf-8"))
        raw_username = client_socket.recv(1024).decode("utf-8").strip()
        username = raw_username if raw_username else f"User{address[1]}"

        with clients_lock:
            clients[client_socket] = username

        print(f"[{timestamp()}] {username} connected from {address}")
        client_socket.sendall(
            f"Welcome, {username}! You are now connected.\n".encode("utf-8")
        )
        broadcast(f"[{timestamp()}] * {username} has joined the chat *\n",
                  exclude_socket=client_socket)

        while True:
            data = client_socket.recv(1024)
            if not data:
                break  # Client disconnected

            text = data.decode("utf-8").strip()
            if not text:
                continue

            formatted = f"[{timestamp()}] {username}: {text}\n"
            print(formatted.strip())
            broadcast(formatted, exclude_socket=client_socket)

    except (ConnectionResetError, ConnectionAbortedError, OSError):
        pass
    finally:
        removed_username = remove_client(client_socket)
        display_name = removed_username or username
        if display_name:
            leave_message = f"[{timestamp()}] * {display_name} has left the chat *\n"
            print(leave_message.strip())
            broadcast(leave_message)


def start_server(host: str = HOST, port: int = PORT) -> None:
    """Starts the chat server and listens indefinitely for new connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Chat server listening on {host}:{port} (Ctrl+C to stop)")

    try:
        while True:
            client_socket, address = server_socket.accept()
            thread = threading.Thread(
                target=handle_client, args=(client_socket, address), daemon=True
            )
            thread.start()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
