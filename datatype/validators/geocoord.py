import re

from .datatype import Datatype
from datatype.datatype_enum import DatatypeEnum

# TODO: Implement other useful methods or use directly geoPy
class Point:
    """
        Describe a decimal degree (dd) geolocated point
    """
    def __init__(self, lat: float, lng: float):
        self._latitude = lat
        self._longitude = lng

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def __str__(self):
        return f"{self.latitude} {self.longitude}"


class Geocoord(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def _validate(self):
        converters = [
            self.convert_dd_format,
            self.convert_dms_format,
            self.convert_WGS84_RDF_format
        ]

        for convert in converters:
            result = convert(self._raw)
            if result is not None:
                assert (len(result) == 2)
                self._repr = Point(*map(lambda item: float(item), result))
                return True

        return False

    def get_type(self):
        return DatatypeEnum.GEOCOORD

    @staticmethod
    def convert_dd_format(s: str):
        """
            Decimal degrees coordinates (e.g. 46.1368155, 9.61057690000007)
        """
        dd_regex = r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)(,|\s)\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$"
        search = re.search(dd_regex, s, flags=re.I | re.M)
        if search is not None:
            return search.group(1), search.group(5)

        return None

    @staticmethod
    def convert_dms_format(s: str):
        """
            Degrees, minutes, seconds coordinates (e.g. 35°56′51″N 75°45′12″E)
            For now I assume NE system
        """
        def convert_to_dd(degrees, minutes, seconds):
            return degrees + minutes/60.0 + seconds/3600.0

        dms_regex = r"^([0-9]+)°\s*([0-9]+)\s*(′|')\s*([0-9]+)\s*(\"|''|′′)\s*([N|S])\s*(,)*\s*([0-9]+)°\s*([0-9]+)\s*(′|')\s*([0-9]+)\s*(\"|''|′′)\s*([W,E])"
        search = re.search(dms_regex, s, flags=re.I | re.M)
        if search is not None:
            lat = tuple(map(lambda item: float(item), (search.group(1), search.group(2), search.group(4))))
            # lat_mod = search.group(6)
            
            lng = tuple(map(lambda item: float(item), (search.group(8), search.group(9), search.group(11))))
            # lng_mod = search.group(13)

            if (-90 <= lat[0] <= 90 and 0 <= lat[1] < 60 and 0 <= lat[2] < 60) and \
               (-90 <= lng[0] <= 90 and 0 <= lng[1] < 60 and 0 <= lng[2] < 60):
                return convert_to_dd(*lat), convert_to_dd(*lng)

        return None            
    
    @staticmethod
    def convert_WGS84_RDF_format(s: str):
        """
            WGS84 RDF coordinates (e.g. POINT(46.1368155 9.61057690000007) )
        """
        wgs84_rdf_regex = r"^POINT\s*\(\s*[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)\s+[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)\s*\)\s*$"
        search = re.search(wgs84_rdf_regex, s, flags=re.I | re.M)
        if search is not None:
            return search.group(1), search.group(4)

        return None