import unittest
from datatype.validators.boolean import Boolean

class TestBoolean(unittest.TestCase):
    def test_true_is_ok(self):
        b = Boolean("true")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, True)

    def test_uppercase_is_ok(self):
        b = Boolean("TrUE")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, True)

    def test_false_is_ok(self):
        b = Boolean("false")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, False)

    def test_y_is_ok(self):
        b = Boolean("y")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, True)

    def test_yes_is_ok(self):
        b = Boolean("yes")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, True)

    def test_n_is_ok(self):
        b = Boolean("n")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, False)

    def test_no_is_ok(self):
        b = Boolean("no")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, False)

    def test_empty_is_bad(self):
        b = Boolean("")

        valid = b.is_valid()

        self.assertFalse(valid)

    def test_2_is_bad(self):
        b = Boolean("2")

        valid = b.is_valid()

        self.assertFalse(valid)

    def test_negative_one_is_bad(self):
        b = Boolean("-1")

        valid = b.is_valid()

        self.assertFalse(valid)