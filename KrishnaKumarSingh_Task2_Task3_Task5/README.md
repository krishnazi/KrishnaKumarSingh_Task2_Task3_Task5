# Python Programming Internship — Completed Tasks

This repository contains my completed tasks for the Python Programming
internship track. Per the completion rule (at least 3 of 5 tasks), the
following three have been completed at the **Beginner Tier**:

| # | Project | Description | Folder |
|---|---------|--------------|--------|
| 1 | 🧮 BMI Calculator | CLI tool to calculate and classify Body Mass Index | [`task-2-bmi-calculator/`](./task-2-bmi-calculator) |
| 2 | 🔐 Random Password Generator | CLI tool to generate strong passwords by custom criteria | [`task-3-password-generator/`](./task-3-password-generator) |
| 3 | 💬 Chat Application | Real-time two-user chat using sockets | [`task-5-chat-application/`](./task-5-chat-application) |

Each folder is a fully self-contained project with its own source code,
unit tests, and detailed README explaining the objective, tech stack,
features, and how to run it.

## 🛠 Tech Stack (overall)

Python 3 (standard library only across all three projects — no external
dependencies to install):
- `input()`, `string`, `random` — BMI Calculator & Password Generator
- `socket`, `threading` — Chat Application

## 🧪 Running Tests

Each project has its own `tests/` folder. From inside any project folder:

```bash
python -m unittest discover tests -v
```

## 📁 Repository Structure

```
KrishnaKumarSingh_Task2_Task3_Task5/
├── task-2-bmi-calculator/
│   ├── bmi_calculator.py
│   ├── tests/test_bmi.py
│   └── README.md
├── task-3-password-generator/
│   ├── password_generator.py
│   ├── tests/test_password_generator.py
│   └── README.md
├── task-5-chat-application/
│   ├── server.py
│   ├── client.py
│   ├── tests/test_integration.py
│   └── README.md
├── README.md          ← you are here
├── .gitignore
└── LICENSE
```

## 📄 License

This repository is licensed under the MIT License — see [LICENSE](LICENSE).
