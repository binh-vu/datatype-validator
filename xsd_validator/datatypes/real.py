from .datatype import Datatype
from xsd_validator.datatype_enum import DatatypeEnum

class Real(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def _validate(self):
        self._raw = self._normalize(self._raw)

        # Not-a-Number is not a real number
        if self._is_NaN(self._raw):
            return False

        try:
            self._repr = float(self._raw)
            return True
        except ValueError:
            return False

    def get_type(self):
        return DatatypeEnum.REAL

    def _is_NaN(self, s: str):
        return s.lower() == "nan"

    def _normalize(self, s: str):
        return s.replace(",", ".")
