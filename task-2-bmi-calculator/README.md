# BMI Calculator (Python CLI)

A simple, robust command-line tool that calculates a user's Body Mass Index
(BMI) and classifies it into standard health categories.

Built as part of a Python Programming internship track (Task 2 — Beginner Tier).

## 📋 Objective

Calculate BMI from user-provided weight and height, and classify the result
into one of the standard WHO health categories, with full input validation.

## 🛠 Tech Stack

- Python 3 (standard library only — no external dependencies)
- `input()` for command-line interaction
- Basic arithmetic for the BMI formula

## ✅ Features

- [x] Prompts user for weight (kg) and height (m) via command line
- [x] Calculates BMI using the formula: `BMI = weight / (height²)`
- [x] Classifies result into standard categories:
  - Underweight: BMI < 18.5
  - Normal weight: 18.5 – 24.9
  - Overweight: 25 – 29.9
  - Obese: ≥ 30
- [x] Displays BMI rounded to 2 decimal places, along with the category
- [x] Input validation — rejects non-numeric and negative/zero input with a
      helpful error message and re-prompts the user
- [x] Loop to calculate BMI for multiple entries without restarting the program

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher (no external packages required)

### Run the program

```bash
git clone https://github.com/krishnazi/KrishnaKumarSingh_Task2_Task3_Task5.git
cd KrishnaKumarSingh_Task2_Task3_Task5/task-2-bmi-calculator
python bmi_calculator.py
```

### Example Session

```
========================================
        BMI CALCULATOR (CLI)
========================================
Enter your weight in kg: 70
Enter your height in m (e.g., 1.75): 1.75

----------------------------------
  Your BMI:      22.86
  Category:      Normal weight
----------------------------------

Calculate another BMI? (y/n): n

Thank you for using the BMI Calculator. Goodbye!
```

## 🧪 Running Tests

Unit tests cover the core calculation and classification logic
(`calculate_bmi` and `classify_bmi`), including category boundary values.

```bash
python -m unittest discover tests -v
```

## 📁 Project Structure

```
bmi-calculator/
├── bmi_calculator.py     # Main program
├── tests/
│   └── test_bmi.py       # Unit tests
├── README.md
├── .gitignore
└── LICENSE
```

## 🔮 Possible Future Enhancements

- GUI version with `tkinter` (color-coded results)
- Save historical BMI records per user (SQLite/CSV)
- BMI trend chart using `matplotlib`

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file.
