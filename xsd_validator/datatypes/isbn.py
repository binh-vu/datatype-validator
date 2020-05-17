import re
import isbnlib

from .datatype import Datatype
from xsd_validator.datatype_enum import DatatypeEnum

class ISBN(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def _validate(self):
        self._raw = isbnlib.canonical(self._raw)

        if isbnlib.is_isbn10(self._raw) or isbnlib.is_isbn13(self._raw):
            self._repr = self._raw
            return True

        return False

    def get_type(self):
        return DatatypeEnum.ISBN