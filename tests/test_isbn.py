import unittest
from datatype.validators.isbn import ISBN

class TestISBN(unittest.TestCase):
    def test_isbn10_is_ok(self):
        b = ISBN("0395595118")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "0395595118")

    def test_isbn13_is_ok(self):
        b = ISBN("9780395595114")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "9780395595114")
    
    def test_isbn13_unstriped_alt_is_ok(self):
        b = ISBN("urn:ISBN:978-2-221-08049-8")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "9782221080498")