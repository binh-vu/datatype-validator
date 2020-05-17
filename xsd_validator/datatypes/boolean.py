from .datatype import Datatype
from xsd_validator.datatype_enum import DatatypeEnum

class Boolean(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def _validate(self):
        self._raw = self._raw.lower()
        truth_table = {
            True: ["y", "yes", "true", "t"],
            False: ["n", "no", "false", "f"]
        }
        for boolean, table in truth_table.items():
            if self._raw in table:
                self._repr = boolean
                return True

        return False

    def get_type(self):
        return DatatypeEnum.BOOLEAN

    def _is_NaN(self, s: str):
        return s.lower() == "nan"

    def _normalize(self, s: str):
        return s.replace(",", ".")
