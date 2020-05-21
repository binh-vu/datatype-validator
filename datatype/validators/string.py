from .datatype import Datatype
from datatype.datatype_enum import DatatypeEnum
import re

def _retain_alpha(s):
    """
        Remove all non alpha characters
    """
    return re.sub(r'[^a-zA-Z]', '', s)

class String(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def _validate(self):
        if len(_retain_alpha(self._raw)) > 0:
            self._repr = self._raw
            return True

        return False

    def get_type(self):
        return DatatypeEnum.STRING

# Dummy
class Unknown(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def _validate(self):
        self._repr = self._raw
        return True

    def get_type(self):
        return DatatypeEnum.UNKNOWN