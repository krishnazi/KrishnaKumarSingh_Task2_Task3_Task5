"""
BMI Calculator (Command-Line Version)
--------------------------------------
Prompts the user for weight (kg) and height (m), calculates their
Body Mass Index, and classifies the result into a standard health
category.

Author: <your name here>
"""


def get_positive_float(prompt: str) -> float:
    """
    Repeatedly prompts the user until a valid, positive numeric value
    is entered. Rejects non-numeric input and negative/zero values.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
        except ValueError:
            print("  ⚠ Invalid input. Please enter a numeric value (e.g., 65.5).")
            continue

        if value <= 0:
            print("  ⚠ Value must be greater than zero. Please try again.")
            continue

        return value


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculates BMI using the standard formula: weight / height^2."""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    """Classifies a BMI value into a standard health category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def print_result(bmi: float, category: str) -> None:
    """Displays the BMI result rounded to 2 decimal places, with category."""
    print("\n----------------------------------")
    print(f"  Your BMI:      {bmi:.2f}")
    print(f"  Category:      {category}")
    print("----------------------------------\n")


def run_calculator() -> None:
    """Main program loop: calculates BMI and offers to repeat."""
    print("=" * 40)
    print("        BMI CALCULATOR (CLI)")
    print("=" * 40)

    while True:
        weight = get_positive_float("Enter your weight in kg: ")
        height = get_positive_float("Enter your height in m (e.g., 1.75): ")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        print_result(bmi, category)

        again = input("Calculate another BMI? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using the BMI Calculator. Goodbye!")
            break


if __name__ == "__main__":
    run_calculator()
