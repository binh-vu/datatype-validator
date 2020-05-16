import unittest
from xsd_validator.datatypes.geocoord import Geocoord, Point

class TestGeocoord(unittest.TestCase):
    def test_dd_valid_format_is_ok(self):
        gc = Geocoord("45.9522, 34.2345")

        valid = gc.validate()
        python_repr = gc.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, Point))
        self.assertAlmostEqual(python_repr.latitude, 45.9522, places=4)
        self.assertAlmostEqual(python_repr.longitude, 34.2345, places=4)

    def test_dms_valid_format_is_ok(self):
        gc = Geocoord("45° 54' 10'' N, 9° 2' 31'' E")

        valid = gc.validate()
        python_repr = gc.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, Point))
        self.assertAlmostEqual(python_repr.latitude, 45.902778, places=6)
        self.assertAlmostEqual(python_repr.longitude, 9.041944, places=6)

    def test_dd_no_space_is_ok(self):
        gc = Geocoord("45.9522,34.2345")

        valid = gc.validate()
        python_repr = gc.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, Point))
        self.assertAlmostEqual(python_repr.latitude, 45.9522, places=4)
        self.assertAlmostEqual(python_repr.longitude, 34.2345, places=4)

    def test_dms_no_space_is_ok(self):
        gc = Geocoord("45°54'10''N,9°2'31''E")

        valid = gc.validate()
        python_repr = gc.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, Point))
        self.assertAlmostEqual(python_repr.latitude, 45.902778, places=6)
        self.assertAlmostEqual(python_repr.longitude, 9.041944, places=6)

    def test_dms_double_quote_is_ok(self):
        gc = Geocoord("45°54'10\"N,9°2'31''E")

        valid = gc.validate()
        python_repr = gc.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, Point))
        self.assertAlmostEqual(python_repr.latitude, 45.902778, places=6)
        self.assertAlmostEqual(python_repr.longitude, 9.041944, places=6)

    def test_dd_no_comma_is_ok(self):
        gc = Geocoord("45.9522 34.2345")

        valid = gc.validate()
        python_repr = gc.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, Point))
        self.assertAlmostEqual(python_repr.latitude, 45.9522, places=4)
        self.assertAlmostEqual(python_repr.longitude, 34.2345, places=4)

    def test_dms_no_comma_is_ok(self):
        gc = Geocoord("45°54'10''N 9°2'31''E")

        valid = gc.validate()
        python_repr = gc.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, Point))
        self.assertAlmostEqual(python_repr.latitude, 45.902778, places=6)
        self.assertAlmostEqual(python_repr.longitude, 9.041944, places=6)

    def test_rdf_format_is_ok(self):
        gc = Geocoord("POINT(45.9522 34.2345)")

        valid = gc.validate()
        python_repr = gc.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, Point))
        self.assertAlmostEqual(python_repr.latitude, 45.9522, places=4)
        self.assertAlmostEqual(python_repr.longitude, 34.2345, places=4)

    def test_rdf_format_with_spaces_is_ok(self):
        gc = Geocoord("POINT ( 45.9522  34.2345 )")

        valid = gc.validate()
        python_repr = gc.to_python()

        self.assertTrue(valid)
        self.assertTrue(isinstance(python_repr, Point))
        self.assertAlmostEqual(python_repr.latitude, 45.9522, places=4)
        self.assertAlmostEqual(python_repr.longitude, 34.2345, places=4)

    def test_dms_out_of_range_degree_is_bad(self):
        gc = Geocoord("-92°12'80''N 9°2'3''E")

        valid = gc.validate()

        self.assertFalse(valid)

    def test_dms_out_of_range_minutes_is_bad(self):
        gc = Geocoord("45°70'10''N 9°2'31''E")

        valid = gc.validate()

        self.assertFalse(valid)

    def test_dms_60_minutes_is_bad(self):
        gc = Geocoord("45°12'10''N 9°60'23''E")

        valid = gc.validate()

        self.assertFalse(valid)

    def test_dms_out_of_range_seconds_is_bad(self):
        gc = Geocoord("45°12'80''N 9°2'3''E")

        valid = gc.validate()

        self.assertFalse(valid)

    def test_dms_60_seconds_is_bad(self):
        gc = Geocoord("45°12'60''N 9°2'3''E")

        valid = gc.validate()

        self.assertFalse(valid)

    def test_one_coord_is_bad(self):
        gc = Geocoord("45.9522,")

        self.assertFalse(gc.validate())

    def test_empty_is_bad(self):
        gc = Geocoord("")

        self.assertFalse(gc.validate())
