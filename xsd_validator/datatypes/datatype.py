class Datatype:
    """
        Base class for all datatypes
    """
    def __init__(self, raw: str):
        self._raw = raw
        self._repr = None

    def validate(self):
        raise NotImplementedError()

    def to_python(self):
        return self._repr