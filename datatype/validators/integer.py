from .datatype import Datatype
from datatype.datatype_enum import DatatypeEnum

class Integer(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def _validate(self):
        self._raw = self._normalize(self._raw)

        try:
            self._repr = int(self._raw)
            return True
        except ValueError:
            return False

    def get_type(self):
        return DatatypeEnum.INTEGER

    def _normalize(self, s: str):
        return s.replace(",", ".")
