import unittest
from datatype.validators.email import Email

class TestEmail(unittest.TestCase):
    def test_generic_email_is_ok(self):
        b = Email("email@mail.com")

        valid = b.is_valid()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "email@mail.com")

    def test_email_have_not_at_symbol_is_bad(self):
        b = Email("emailmail.com")

        valid = b.is_valid()

        self.assertFalse(valid)

    def test_email_have_not_domain_is_bad(self):
        b = Email("email@mail")

        valid = b.is_valid()

        self.assertFalse(valid)
