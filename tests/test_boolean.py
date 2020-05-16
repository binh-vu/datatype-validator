import unittest
from xsd_validator.datatypes.boolean import Boolean

class TestBoolean(unittest.TestCase):
    def test_true_is_ok(self):
        b = Boolean("true")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, True)

    def test_uppercase_is_ok(self):
        b = Boolean("TrUE")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, True)

    def test_false_is_ok(self):
        b = Boolean("false")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, False)

    def test_y_is_ok(self):
        b = Boolean("y")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, True)

    def test_yes_is_ok(self):
        b = Boolean("yes")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, True)

    def test_n_is_ok(self):
        b = Boolean("n")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, False)

    def test_no_is_ok(self):
        b = Boolean("no")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, False)

    def test_empty_is_bad(self):
        b = Boolean("")

        valid = b.validate()

        self.assertFalse(valid)

    def test_2_is_bad(self):
        b = Boolean("2")

        valid = b.validate()

        self.assertFalse(valid)

    def test_negative_one_is_bad(self):
        b = Boolean("-1")

        valid = b.validate()

        self.assertFalse(valid)