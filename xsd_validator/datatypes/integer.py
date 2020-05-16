from .datatype import Datatype

class Integer(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def validate(self):
        self._raw = self._normalize(self._raw)

        try:
            self._repr = int(self._raw)
            return True
        except ValueError:
            return False

    def _normalize(self, s: str):
        return s.replace(",", ".")
