from enum import Enum
from datatype.xsd import anyURI, boolean, date, numeric, string, geo

class DatatypeEnum(Enum):
    INTEGER = "integer"
    REAL = "real"
    BOOLEAN = "boolean"
    STRING = "string"
    DATE = "date"
    URL = "url"
    EMAIL = "email"
    ISBN = "isbn"
    GEOCOORD = "geo_coordinates"
    UNKNOWN = "unknown"

    @staticmethod
    def get_datatype_info(data_type):
        datatype_map = {
            DatatypeEnum.INTEGER: numeric.XsdNumeric(),
            DatatypeEnum.REAL: numeric.XsdNumeric(),
            DatatypeEnum.BOOLEAN: boolean.XsdBoolean(),
            DatatypeEnum.STRING: string.XsdString(),
            DatatypeEnum.DATE: date.XsdDate(),
            DatatypeEnum.URL: anyURI.XsdUri(),
            DatatypeEnum.EMAIL: string.XsdString(),
            DatatypeEnum.ISBN: string.XsdString(),
            DatatypeEnum.GEOCOORD: geo.XsdGeo(),
            DatatypeEnum.UNKNOWN: string.XsdString(),
        }

        return datatype_map.get(data_type, string.XsdString())

    @staticmethod
    def get_datatype_uri(data_type):
        all_datatype = [
            {
                "label": "xsd:string",
                "uri": "http://www.w3.org/2001/XMLSchema#string"
            },
            {
                "label": "xsd:float",
                "uri": "http://www.w3.org/2001/XMLSchema#float"
            },
            {
                "label": "xsd:integer",
                "uri": "http://www.w3.org/2001/XMLSchema#integer"
            },
            {
                "label": "xsd:double",
                "uri": "http://www.w3.org/2001/XMLSchema#double"
            },
            {
                "label": "xsd:date",
                "uri": "http://www.w3.org/2001/XMLSchema#date"
            },
            {
                "label": "xsd:boolean",
                "uri": "http://www.w3.org/2001/XMLSchema#boolean"
            },
            {
                "label": "xsd:anyURI",
                "uri": "http://www.w3.org/2001/XMLSchema#anyURI"
            }
        ]

        for current_type in all_datatype:
            if current_type['label'] == data_type:
                return current_type
