# Random Password Generator (Python CLI)

A simple, robust command-line tool that generates strong, random passwords
based on user-defined criteria: length and character types.

Built as part of a Python Programming internship track (Task 3 — Beginner Tier).

## 📋 Objective

Generate a random password matching user-specified criteria (length and
character types), with full input validation and the ability to generate
multiple passwords in one session.

## 🛠 Tech Stack

- Python 3 (standard library only — no external dependencies)
- `random` — for random character selection
- `string` — for character set constants (letters, digits, punctuation)

## ✅ Features

- [x] Prompts user for desired password length (minimum 8 characters enforced)
- [x] Prompts user to choose character types to include: uppercase,
      lowercase, numbers, symbols (at least 2 types required)
- [x] Generates and displays a password matching the specified criteria
- [x] Input validation — rejects invalid lengths (non-numeric or < 8) and
      rejects selections with fewer than 2 character types, with helpful
      error messages and re-prompting
- [x] Option to generate another password without restarting the program

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher (no external packages required)

### Run the program

```bash
git clone https://github.com/krishnazi/KrishnaKumarSingh_Task2_Task3_Task5.git
cd KrishnaKumarSingh_Task2_Task3_Task5/task-3-password-generator
python password_generator.py
```

### Example Session

```
=============================================
        RANDOM PASSWORD GENERATOR (CLI)
=============================================
Enter desired password length (minimum 8): 12

Which character types should the password include?
  (u) Uppercase letters  (A-Z)
  (l) Lowercase letters  (a-z)
  (n) Numbers            (0-9)
  (s) Symbols            (!@#$...)
Enter your choices as letters, e.g. 'uln': uln

----------------------------------------------
  Character types used: uppercase letters, lowercase letters, numbers
  Generated password:   Kq3Rz9pLmT2v
----------------------------------------------

Generate another password? (y/n): n

Thank you for using the Password Generator. Goodbye!
```

## 🧪 Running Tests

Unit tests cover the core logic: building character pools from selected
types, and generating passwords of the correct length using only characters
from the selected pool.

```bash
python -m unittest discover tests -v
```

## 📁 Project Structure

```
password-generator/
├── password_generator.py     # Main program
├── tests/
│   └── test_password_generator.py   # Unit tests
├── README.md
├── .gitignore
└── LICENSE
```

## ⚠️ Security Note

This generator uses Python's `random` module, which is suitable for
demos and learning purposes but is **not cryptographically secure**.
For production or security-sensitive use, use the `secrets` module instead
(this is exactly what the Advanced Tier of this task requires).

## 🔮 Possible Future Enhancements

- GUI version with `tkinter` (sliders, checkboxes)
- Cryptographically secure generation using the `secrets` module
- Password strength indicator (Weak / Medium / Strong)
- Guarantee at least one character from each selected type
- "Copy to Clipboard" support via `pyperclip`
- Option to exclude ambiguous characters (0, O, l, 1)

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file.
