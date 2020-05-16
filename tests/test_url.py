import unittest
from xsd_validator.datatypes.url import Url

class TestUrl(unittest.TestCase):
    def test_generic_url_is_ok(self):
        b = Url("http://www.example.com")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "http://www.example.com")

    def test_https_url_is_ok(self):
        b = Url("https://www.example.com")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "https://www.example.com")

    def test_url_with_query_is_ok(self):
        b = Url("http://www.example.com?q=hello&u=1")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "http://www.example.com?q=hello&u=1")

    def test_no_www_url_is_ok(self):
        b = Url("http://example.com")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "http://example.com")

    def test_empty_url_is_bad(self):
        b = Url("")

        valid = b.validate()

        self.assertFalse(valid)

    def test_no_domain_is_bad(self):
        b = Url("http://example")

        valid = b.validate()

        self.assertFalse(valid)

    # TODO: No it should not be bad...
    def test_not_http_is_bad(self):
        b = Url("www.example.com")

        valid = b.validate()

        self.assertFalse(valid)