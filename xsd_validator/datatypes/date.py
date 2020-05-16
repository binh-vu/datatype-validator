import re
import calendar
from datetime import datetime

from xsd_validator.datatypes.datatype import Datatype

# TODO: use also dateutils library to parse more sophisticated formats
class Date(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def validate(self):
        converters = [
            self.convert_dmy_date,
            self.convert_mdy_date,
            self.convert_ydm_date
        ]

        for convert in converters:
            result = convert(self._raw)
            if result is not None:
                assert (len(result) == 3)
                self._repr = datetime(result[2], result[1], result[0], 0, 0)
                return True

        return False

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
                        return day, month, year

        return None
