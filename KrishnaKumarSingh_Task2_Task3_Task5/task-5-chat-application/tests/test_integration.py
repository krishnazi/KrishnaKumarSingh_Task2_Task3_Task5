"""
Integration tests for server.py

These tests start the real chat server on a background thread and
connect to it with raw sockets (bypassing client.py's input() loop)
to verify: connection handling, username registration, message
broadcasting with timestamps, and disconnection notifications.

Run with:
    python -m unittest discover tests -v
"""

import socket
import threading
import time
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server import start_server

TEST_HOST = "127.0.0.1"
TEST_PORT = 6060  # Different from the default 5555 to avoid clashes


def make_client() -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TEST_HOST, TEST_PORT))
    return sock


class TestChatServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the server once for all tests in this class.
        server_thread = threading.Thread(
            target=start_server, args=(TEST_HOST, TEST_PORT), daemon=True
        )
        server_thread.start()
        time.sleep(0.3)  # give the server a moment to start listening

    def _login(self, sock: socket.socket, username: str) -> None:
        """Handles the username prompt/response handshake."""
        prompt = sock.recv(1024).decode("utf-8")
        self.assertIn("Enter your username", prompt)
        sock.sendall(username.encode("utf-8"))
        welcome = sock.recv(1024).decode("utf-8")
        self.assertIn("Welcome", welcome)

    def test_two_clients_can_connect_and_exchange_messages(self):
        alice = make_client()
        self._login(alice, "Alice")

        bob = make_client()
        self._login(bob, "Bob")

        # Alice should be notified that Bob joined
        join_notice = alice.recv(1024).decode("utf-8")
        self.assertIn("Bob has joined the chat", join_notice)

        # Alice sends a message; Bob should receive it with a timestamp prefix
        alice.sendall(b"Hello Bob!")
        time.sleep(0.2)
        received = bob.recv(1024).decode("utf-8")
        self.assertIn("Alice: Hello Bob!", received)
        self.assertRegex(received, r"^\[\d{2}:\d{2}\]")

        alice.close()
        bob.close()

    def test_disconnection_notifies_other_client(self):
        carol = make_client()
        self._login(carol, "Carol")

        dave = make_client()
        self._login(dave, "Dave")

        # Clear Carol's "Dave has joined" notice
        carol.recv(1024)

        # Dave disconnects
        dave.close()
        time.sleep(0.3)

        leave_notice = carol.recv(1024).decode("utf-8")
        self.assertIn("Dave has left the chat", leave_notice)

        carol.close()

    def test_bidirectional_messaging(self):
        eve = make_client()
        self._login(eve, "Eve")

        frank = make_client()
        self._login(frank, "Frank")

        eve.recv(1024)  # clear join notice

        # Eve -> Frank
        eve.sendall(b"Hi Frank")
        time.sleep(0.2)
        msg1 = frank.recv(1024).decode("utf-8")
        self.assertIn("Eve: Hi Frank", msg1)

        # Frank -> Eve
        frank.sendall(b"Hi Eve")
        time.sleep(0.2)
        msg2 = eve.recv(1024).decode("utf-8")
        self.assertIn("Frank: Hi Eve", msg2)

        eve.close()
        frank.close()


if __name__ == "__main__":
    unittest.main()
