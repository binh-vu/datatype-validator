import unittest
from xsd_validator.datatypes.integer import Integer

class TestInteger(unittest.TestCase):
    def test_positive_integer_is_ok(self):
        b = Integer("10")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, int))
        self.assertEqual(python_repr, 10)

    def test_negative_integer_is_ok(self):
        b = Integer("-10")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, int))
        self.assertEqual(python_repr, -10)

    def test_zero_is_ok(self):
        b = Integer("0")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, int))
        self.assertEqual(python_repr, 0)

    def test_exp_is_bad(self):
        b = Integer("1E3")

        valid = b.validate()

        self.assertFalse(valid)

    def test_one_is_ok(self):
        b = Integer("1")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, int))
        self.assertEqual(python_repr, 1)

    def test_float_is_bad(self):
        b = Integer("10.0")

        valid = b.validate()

        self.assertFalse(valid)

    def test_NaN_is_bad(self):
        b = Integer("NaN")

        valid = b.validate()

        self.assertFalse(valid)

    def test_alpha_string_is_bad(self):
        b = Integer("hello")

        valid = b.validate()

        self.assertFalse(valid)

    def test_alphanumeric_string_is_bad(self):
        b = Integer("hello3")

        valid = b.validate()

        self.assertFalse(valid)

    def test_empty_is_bad(self):
        b = Integer("")

        valid = b.validate()

        self.assertFalse(valid)