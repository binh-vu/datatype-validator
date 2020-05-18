from datatype.datatype_enum import DatatypeEnum

class Datatype:
    """
        Base class for all datatypes
    """
    def __init__(self, raw: str):
        self._raw = raw
        self._repr = None
        self._is_valid = self._validate()

    def is_valid(self):
        return self._is_valid

    def to_python(self):
        return self._repr

    def get_type(self):
        raise NotImplementedError()

    def get_xsd_type(self):
        return DatatypeEnum.get_datatype_info(self.get_type())

    def _validate(self):
        raise NotImplementedError()