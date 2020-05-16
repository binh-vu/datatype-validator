import unittest
from xsd_validator.datatypes.email import Email

class TestEmail(unittest.TestCase):
    def test_generic_email_is_ok(self):
        b = Email("email@mail.com")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "email@mail.com")

    def test_email_have_not_at_symbol_is_bad(self):
        b = Email("emailmail.com")

        valid = b.validate()

        self.assertFalse(valid)

    def test_email_have_not_domain_is_bad(self):
        b = Email("email@mail")

        valid = b.validate()

        self.assertFalse(valid)
