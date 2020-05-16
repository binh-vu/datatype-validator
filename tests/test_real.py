import unittest
from xsd_validator.datatypes.real import Real

class TestReal(unittest.TestCase):
    def test_positive_real_is_ok(self):
        b = Real("10.0")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, float))
        self.assertAlmostEqual(python_repr, 10.0, places=3)

    def test_negative_real_is_ok(self):
        b = Real("-10.0")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, float))
        self.assertAlmostEqual(python_repr, -10.0, places=3)

    def test_exp_is_ok(self):
        b = Real("1.3E3")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, float))
        self.assertAlmostEqual(python_repr, 1300.0, places=3)

    def test_zero_is_ok(self):
        b = Real("0.0")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, float))
        self.assertAlmostEqual(python_repr, 0.0, places=3)

    def test_one_is_ok(self):
        b = Real("1.0")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, float))
        self.assertAlmostEqual(python_repr, 1.0, places=3)

    def test_NaN_is_bad(self):
        b = Real("NaN")

        valid = b.validate()

        self.assertFalse(valid)

    def test_alpha_string_is_bad(self):
        b = Real("hello")

        valid = b.validate()

        self.assertFalse(valid)

    def test_alphanumeric_string_is_bad(self):
        b = Real("hello3")

        valid = b.validate()

        self.assertFalse(valid)

    def test_empty_is_bad(self):
        b = Real("")

        valid = b.validate()

        self.assertFalse(valid)