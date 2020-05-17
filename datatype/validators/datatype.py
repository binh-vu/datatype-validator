class Datatype:
    """
        Base class for all datatypes
    """
    def __init__(self, raw: str):
        self._raw = raw
        self._repr = None
        self._is_valid = self._validate()

    def is_valid(self):
        return self._is_valid

    def to_python(self):
        return self._repr

    def get_type(self):
        raise NotImplementedError()

    def _validate(self):
        raise NotImplementedError()