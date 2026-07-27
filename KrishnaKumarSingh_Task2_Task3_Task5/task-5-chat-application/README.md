# Chat Application (Python Sockets)

A real-time, two-user chat application built with Python's `socket` and
`threading` modules — no external dependencies required.

Built as part of a Python Programming internship track (Task 5 — Beginner Tier).

## 📋 Objective

Build a real-time messaging application: a server that listens for client
connections, and a client that connects and exchanges messages
bidirectionally, with timestamps and graceful disconnection handling.

## 🛠 Tech Stack

- Python 3 (standard library only)
- `socket` — TCP client/server networking
- `threading` — handling multiple clients and simultaneous send/receive

## ✅ Features

- [x] Server script listens for incoming client connections
- [x] Client script connects to the server
- [x] Real-time, bidirectional message exchange between connected clients
- [x] Messages displayed with a timestamp prefix, e.g. `[14:35] Alice: Hello`
- [x] Graceful disconnection handling — the other client is notified when
      one disconnects (e.g. `* Bob has left the chat *`)
- [x] Both scripts run on the same machine using `localhost` (127.0.0.1)

**Bonus (beyond the minimum requirement):** the server supports more than
two simultaneous clients — any connected client's messages are broadcast to
everyone else, so you can test with 2, 3, or more terminals at once.

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher (no external packages required)

### Run it locally (3 terminals)

**Terminal 1 — start the server:**
```bash
git clone https://github.com/krishnazi/KrishnaKumarSingh_Task2_Task3_Task5.git
cd KrishnaKumarSingh_Task2_Task3_Task5/task-5-chat-application
python server.py
```
You should see:
```
Chat server listening on 127.0.0.1:5555 (Ctrl+C to stop)
```

**Terminal 2 — first client:**
```bash
python client.py
```

**Terminal 3 — second client:**
```bash
python client.py
```

Each client will be prompted for a username. Once both are connected,
anything typed in one terminal appears in the other, with a timestamp
and sender name. Type `/quit` or `/exit` in a client to leave the chat —
the other client will see a "has left the chat" notice.

### Example Session

**Terminal 2 (Alice):**
```
Enter your username: Alice
Welcome, Alice! You are now connected.
Connected! Type your messages below. Type /quit to leave.

[14:35] * Bob has joined the chat *
Hey Bob!
[14:36] Bob: Hey Alice, how's it going?
```

**Terminal 3 (Bob):**
```
Enter your username: Bob
Welcome, Bob! You are now connected.
Connected! Type your messages below. Type /quit to leave.

[14:35] Alice: Hey Bob!
Hey Alice, how's it going?
```

## 🧪 Running Tests

Since this app requires two live connections to test properly, the test
suite starts the real server on a background thread and connects to it
using raw sockets — verifying username handshakes, message broadcasting
with correct timestamp formatting, and disconnection notifications, all
against the actual networking code (not mocks).

```bash
python -m unittest discover tests -v
```

## 📁 Project Structure

```
chat-application/
├── server.py                  # Chat server (accepts connections, broadcasts messages)
├── client.py                  # Chat client (connects, sends/receives messages)
├── tests/
│   └── test_integration.py    # Integration tests using real sockets
├── README.md
├── .gitignore
└── LICENSE
```

## ⚠️ Security Note

This is a learning project: messages are sent as **plain, unencrypted
text** over the socket connection, and there is no authentication. It is
intended for local/trusted-network use only. The Advanced Tier of this
task (GUI, login system, encrypted awareness documentation) addresses
these concerns.

## 🔮 Possible Future Enhancements

- GUI chat window with `tkinter`
- User registration/login backed by SQLite
- Multiple named chat rooms
- Persisted message history
- Desktop notifications for new messages

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file.
