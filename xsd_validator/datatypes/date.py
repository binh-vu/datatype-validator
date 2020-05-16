import re
import calendar
from datetime import datetime
import dateutil.parser

from xsd_validator.datatypes.datatype import Datatype
from xsd_validator.datatypes.real import Real

# TODO: use also dateutils library to parse more sophisticated formats
class Date(Datatype):
    def __init__(self, raw: str):
        super().__init__(raw)

    def validate(self):
        converters = [
            self.convert_dmy_date,
            self.convert_mdy_date,
            self.convert_ydm_date,
            self.convert_generic_date
        ]

        for convert in converters:
            result = convert(self._raw)
            if result is not None:
                self._repr = result
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
    def convert_generic_date(s: str):
        if not Real(s).validate():
            try:
                return dateutil.parser.parse(s, fuzzy_with_tokens=True)[0]
            except (ValueError, OverflowError):
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
