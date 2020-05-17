import unittest
from datatype.validate import get_datatype
from datatype.datatype_enum import DatatypeEnum
from datatype.validators import geocoord

from datetime import datetime

class TestValidate(unittest.TestCase):
    def test_boolean_is_ok(self):
        dt = get_datatype("true")

        valid = dt.is_valid()
        python_repr = dt.to_python()
        dt_type = dt.get_type()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, bool))
        self.assertEqual(python_repr, True)
        self.assertEqual(dt_type, DatatypeEnum.BOOLEAN)

    def test_integer_is_ok(self):
        dt = get_datatype("234")

        valid = dt.is_valid()
        python_repr = dt.to_python()
        dt_type = dt.get_type()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, int))
        self.assertEqual(python_repr, 234)
        self.assertEqual(dt_type, DatatypeEnum.INTEGER)

    def test_real_is_ok(self):
        dt = get_datatype("23.4")

        valid = dt.is_valid()
        python_repr = dt.to_python()
        dt_type = dt.get_type()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, float))
        self.assertEqual(python_repr, 23.4)
        self.assertEqual(dt_type, DatatypeEnum.REAL)

    def test_string_is_ok(self):
        dt = get_datatype("hello")

        valid = dt.is_valid()
        python_repr = dt.to_python()
        dt_type = dt.get_type()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "hello")
        self.assertEqual(dt_type, DatatypeEnum.STRING)

    def test_date_is_ok(self):
        dt = get_datatype("25/12/2020")

        valid = dt.is_valid()
        python_repr = dt.to_python()
        dt_type = dt.get_type()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, datetime))
        self.assertEqual(python_repr, datetime(2020, 12, 25, 0, 0, 0))
        self.assertEqual(dt_type, DatatypeEnum.DATE)

    def test_email_is_ok(self):
        dt = get_datatype("mail@mail.com")

        valid = dt.is_valid()
        python_repr = dt.to_python()
        dt_type = dt.get_type()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "mail@mail.com")
        self.assertEqual(dt_type, DatatypeEnum.EMAIL)

    def test_url_is_ok(self):
        dt = get_datatype("http://example.com")

        valid = dt.is_valid()
        python_repr = dt.to_python()
        dt_type = dt.get_type()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "http://example.com")
        self.assertEqual(dt_type, DatatypeEnum.URL)

    def test_isbn_is_ok(self):
        dt = get_datatype("ISBN:978-2-221-08049-8")

        valid = dt.is_valid()
        python_repr = dt.to_python()
        dt_type = dt.get_type()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, str))
        self.assertEqual(python_repr, "9782221080498")
        self.assertEqual(dt_type, DatatypeEnum.ISBN)

    def test_geocoord_is_ok(self):
        dt = get_datatype("45.3, 9.01")

        valid = dt.is_valid()
        python_repr = dt.to_python()
        dt_type = dt.get_type()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, geocoord.Point))
        self.assertAlmostEqual(python_repr.latitude, 45.3, places=2)
        self.assertAlmostEqual(python_repr.longitude, 9.01, places=2)
        self.assertEqual(dt_type, DatatypeEnum.GEOCOORD)