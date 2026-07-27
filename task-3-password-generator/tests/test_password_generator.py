"""
Unit tests for password_generator.py

Run with:
    python -m unittest discover tests
"""

import unittest
import sys
import os
import string

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from password_generator import build_character_pool, generate_password, CHARACTER_SETS


class TestBuildCharacterPool(unittest.TestCase):
    def test_single_type(self):
        pool = build_character_pool(["n"])
        self.assertEqual(pool, string.digits)

    def test_multiple_types(self):
        pool = build_character_pool(["u", "l"])
        self.assertEqual(pool, string.ascii_uppercase + string.ascii_lowercase)

    def test_all_types(self):
        pool = build_character_pool(["u", "l", "n", "s"])
        expected = (
            string.ascii_uppercase
            + string.ascii_lowercase
            + string.digits
            + string.punctuation
        )
        self.assertEqual(pool, expected)


class TestGeneratePassword(unittest.TestCase):
    def test_correct_length(self):
        pool = build_character_pool(["u", "n"])
        password = generate_password(12, pool)
        self.assertEqual(len(password), 12)

    def test_characters_come_from_pool(self):
        pool = build_character_pool(["l", "s"])
        password = generate_password(50, pool)
        self.assertTrue(all(ch in pool for ch in password))

    def test_digits_only_pool(self):
        pool = build_character_pool(["n"])
        password = generate_password(20, pool)
        self.assertTrue(all(ch in string.digits for ch in password))

    def test_randomness_varies(self):
        # Not a strict guarantee, but two generations of reasonable
        # length should very rarely be identical.
        pool = build_character_pool(["u", "l", "n", "s"])
        password_a = generate_password(16, pool)
        password_b = generate_password(16, pool)
        self.assertNotEqual(password_a, password_b)


if __name__ == "__main__":
    unittest.main()
