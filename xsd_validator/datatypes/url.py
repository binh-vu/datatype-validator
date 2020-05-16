import re
from urllib.parse import unquote

from .datatype import Datatype

class Url(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def validate(self):
        self._raw = unquote(self._raw)

        # NOTE: regex does not match urls without http header
        url_regex = r"(https?):\/\/(www\.)?([-a-zA-Z0-9@:%._\+~#=]{1,256})\.([a-z]{2,6})\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
        search = re.search(url_regex, self._raw.lower(), re.M)

        if search is not None:
            self._repr = self._raw
            return True

        return False