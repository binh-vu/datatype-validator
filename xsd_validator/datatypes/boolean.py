from xsd_validator.datatypes.datatype import Datatype

class Boolean(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def validate(self):
        self._raw = self._raw.lower()
        truth_table = {
            True: ["y", "yes", "1", "true", "t"],
            False: ["n", "no", "0", "false", "f"]
        }
        for boolean, table in truth_table.items():
            if self._raw in table:
                self._repr = boolean
                return True

        return False

    def _is_NaN(self, s: str):
        return s.lower() == "nan"

    def _normalize(self, s: str):
        return s.replace(",", ".")
