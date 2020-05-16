import unittest
from xsd_validator.datatypes.date import Date
from datetime import datetime, timezone
import iso8601

class TestDate(unittest.TestCase):
    def test_iso_date_format_is_ok(self):
        b = Date("01/01/2000")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, datetime))
        self.assertEqual(python_repr, datetime(2000, 1, 1))

    def test_iso_date_alt_format_is_ok(self):
        b = Date("01-01-2000")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, datetime))
        self.assertEqual(python_repr, datetime(2000, 1, 1))

    def test_mdy_format_is_ok(self):
        b = Date("01/25/2000")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, datetime))
        self.assertEqual(python_repr, datetime(2000, 1, 25))

    def test_ydm_format_is_ok(self):
        b = Date("2000/25/1")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, datetime))
        self.assertEqual(python_repr, datetime(2000, 1, 25))

    def test_out_of_range_day_is_bad(self):
        b = Date("56/2/2000")

        valid = b.validate()

        self.assertFalse(valid)

    def test_out_of_range_month_is_bad(self):
        b = Date("13/13/2000")

        valid = b.validate()

        self.assertFalse(valid)

    def test_out_of_range_year_is_bad(self):
        b = Date("1/2/-3")

        valid = b.validate()

        self.assertFalse(valid)

    def test_leap_year_has_29_on_feb_is_ok(self):
        b = Date("29/2/2000")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, datetime))
        self.assertEqual(python_repr, datetime(2000, 2, 29))

    def test_iso8601_is_ok(self):
        b = Date("2016-01-01T00:00:00Z")

        valid = b.validate()
        python_repr = b.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, datetime))
        self.assertEqual(python_repr, datetime(2016, 1, 1, tzinfo=timezone.utc))