from enum import Enum

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

    @staticmethod
    def get_datatype_info(data_type):
        xml_string = {
            "label": "xsd:string",
            "uri": "http://www.w3.org/2001/XMLSchema#string"
        }
        xml_float = {
            "label": "xsd:float",
            "uri": "http://www.w3.org/2001/XMLSchema#float"
        }
        xml_integer = {
            "label": "xsd:integer",
            "uri": "http://www.w3.org/2001/XMLSchema#integer"
        }
        xml_double = {
            "label": "xsd:double",
            "uri": "http://www.w3.org/2001/XMLSchema#double"
        }
        xml_date = {
            "label": "xsd:date",
            "uri": "http://www.w3.org/2001/XMLSchema#date"
        }
        xml_boolean = {
            "label": "xsd:boolean",
            "uri": "http://www.w3.org/2001/XMLSchema#boolean"
        }
        xml_any_uri = {
            "label": "xsd:anyURI",
            "uri": "http://www.w3.org/2001/XMLSchema#anyURI"
        }

        datatype_map = {
            DatatypeEnum.INTEGER: xml_integer,
            DatatypeEnum.REAL: [xml_float, xml_double],
            DatatypeEnum.BOOLEAN: xml_boolean,
            DatatypeEnum.STRING: xml_string,
            DatatypeEnum.DATE: xml_date,
            DatatypeEnum.URL: xml_any_uri,
            DatatypeEnum.EMAIL: xml_string,
            DatatypeEnum.ISBN: xml_string,
            DatatypeEnum.GEOCOORD: xml_string,
        }

        return datatype_map.get(data_type, xml_string)

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
