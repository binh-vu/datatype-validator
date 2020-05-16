from xsd_validator.datatypes.datatype import Datatype

class String(Datatype):
    def __init__(self, raw):
        super(String).__init__(raw)

    def validate(self):
        self._repr = self._raw
        return True

