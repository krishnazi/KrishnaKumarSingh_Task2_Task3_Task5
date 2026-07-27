"""
Unit tests for bmi_calculator.py

Run with:
    python -m unittest discover tests
"""

import unittest
import sys
import os

# Allow importing bmi_calculator.py from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bmi_calculator import calculate_bmi, classify_bmi


class TestCalculateBMI(unittest.TestCase):
    def test_known_value(self):
        # 70 kg, 1.75 m -> BMI = 70 / (1.75**2) = 22.857...
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.857, places=2)

    def test_small_height(self):
        self.assertAlmostEqual(calculate_bmi(50, 1.0), 50.0)


class TestClassifyBMI(unittest.TestCase):
    def test_underweight(self):
        self.assertEqual(classify_bmi(17.0), "Underweight")

    def test_normal_lower_bound(self):
        self.assertEqual(classify_bmi(18.5), "Normal weight")

    def test_normal_upper_bound(self):
        self.assertEqual(classify_bmi(24.9), "Normal weight")

    def test_overweight(self):
        self.assertEqual(classify_bmi(27.0), "Overweight")

    def test_obese_boundary(self):
        self.assertEqual(classify_bmi(30.0), "Obese")

    def test_obese_high(self):
        self.assertEqual(classify_bmi(40.0), "Obese")


if __name__ == "__main__":
    unittest.main()
