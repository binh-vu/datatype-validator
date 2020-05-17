import re
import calendar
from datetime import datetime
import iso8601

from .datatype import Datatype
from .real import Real
from datatype.datatype_enum import DatatypeEnum

# TODO: use also dateutils library to parse more sophisticated formats
class Date(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def _validate(self):
        converters = [
            self.convert_dmy_date,
            self.convert_mdy_date,
            self.convert_ydm_date,
            self.convert_iso8601_date,
        ]

        for convert in converters:
            result = convert(self._raw)
            if result is not None:
                self._repr = result
                return True

        return False

    def get_type(self):
        return DatatypeEnum.DATE

    @staticmethod
    def convert_dmy_date(s: str):
        dmy_regex = r"^([0-9]{1,2})(-|/)([0-9]{1,2})(-|/)([0-9]{1,4})$"
        return Date._convert_date(dmy_regex, s, [1, 3, 5])

    @staticmethod
    def convert_mdy_date(s: str):
        mdy_regex = r"^([0-9]{1,2})(-|/)([0-9]{1,2})(-|/)([0-9]{1,4})$"
        return Date._convert_date(mdy_regex, s, [3, 1, 5])

    @staticmethod
    def convert_ydm_date(s: str):
        ydm_regex = r"^([0-9]{1,4})(-|/)([0-9]{1,2})(-|/)([0-9]{1,2})$"
        return Date._convert_date(ydm_regex, s, [3, 5, 1])


    @staticmethod
    def convert_iso8601_date(s: str):
        if not Real(s).is_valid():
            try:
                return iso8601.parse_date(s)
            except (iso8601.ParseError, ValueError, OverflowError, TypeError):
                return None
        return None

    @staticmethod
    def _convert_date(regex: str, s: str, group):
        search = re.search(regex, s)
        if search is not None:
            day, month, year = tuple(
                int(search.group(group_id))
                for group_id in group
            )
            if year > 0:
                if 1 <= month <= 12:
                    if 1 <= day <= calendar.monthrange(year, month)[1]:
                        return datetime(year, month, day, 0, 0)

        return None
