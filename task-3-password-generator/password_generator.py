"""
Random Password Generator (Command-Line Version)
--------------------------------------------------
Generates a strong, random password based on user-defined criteria:
desired length and character types to include (uppercase, lowercase,
numbers, symbols).

Author: <Krishna Kuamr Singh>
"""

import random
import string

MIN_LENGTH = 8

CHARACTER_SETS = {
    "u": ("uppercase letters", string.ascii_uppercase),
    "l": ("lowercase letters", string.ascii_lowercase),
    "n": ("numbers", string.digits),
    "s": ("symbols", string.punctuation),
}


def get_valid_length() -> int:
    """
    Prompts the user for a password length, enforcing a minimum of
    MIN_LENGTH characters. Rejects non-numeric or too-short input.
    """
    while True:
        raw_value = input(f"Enter desired password length (minimum {MIN_LENGTH}): ").strip()
        try:
            length = int(raw_value)
        except ValueError:
            print("  ⚠ Invalid input. Please enter a whole number (e.g., 12).")
            continue

        if length < MIN_LENGTH:
            print(f"  ⚠ Length must be at least {MIN_LENGTH} characters. Please try again.")
            continue

        return length


def select_character_types() -> list:
    """
    Asks the user which character types to include (uppercase, lowercase,
    numbers, symbols). Requires at least 2 types to be selected.
    """
    while True:
        print("\nWhich character types should the password include?")
        print("  (u) Uppercase letters  (A-Z)")
        print("  (l) Lowercase letters  (a-z)")
        print("  (n) Numbers            (0-9)")
        print("  (s) Symbols            (!@#$...)")
        raw_choice = input("Enter your choices as letters, e.g. 'uln': ").strip().lower()

        selected = [c for c in raw_choice if c in CHARACTER_SETS]
        selected = list(dict.fromkeys(selected))  # remove duplicates, preserve order

        if len(selected) < 2:
            print("  ⚠ Please select at least 2 different character types.")
            continue

        return selected


def build_character_pool(selected_types: list) -> str:
    """Builds the combined pool of characters based on the selected types."""
    return "".join(CHARACTER_SETS[t][1] for t in selected_types)


def generate_password(length: int, pool: str) -> str:
    """Generates a random password of the given length from the given pool."""
    return "".join(random.choice(pool) for _ in range(length))


def describe_selection(selected_types: list) -> str:
    """Returns a human-readable summary of the selected character types."""
    return ", ".join(CHARACTER_SETS[t][0] for t in selected_types)


def run_generator() -> None:
    """Main program loop: generates passwords and offers to repeat."""
    print("=" * 45)
    print("        RANDOM PASSWORD GENERATOR (CLI)")
    print("=" * 45)

    while True:
        length = get_valid_length()
        selected_types = select_character_types()
        pool = build_character_pool(selected_types)
        password = generate_password(length, pool)

        print("\n----------------------------------------------")
        print(f"  Character types used: {describe_selection(selected_types)}")
        print(f"  Generated password:   {password}")
        print("----------------------------------------------\n")

        again = input("Generate another password? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using the Password Generator. Goodbye!")
            break


if __name__ == "__main__":
    run_generator()
