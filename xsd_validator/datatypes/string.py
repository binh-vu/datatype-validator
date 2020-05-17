from .datatype import Datatype
from xsd_validator.datatype_enum import DatatypeEnum

class String(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def _validate(self):
        self._repr = self._raw
        return True

    def get_type(self):
        return DatatypeEnum.STRING