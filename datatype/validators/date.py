import re
import calendar
from datetime import datetime, timezone
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
            self.convert_ymd_date,
            self.convert_iso8601_date,
            self.convert_wikidata_date,
            self.convert_human_date,
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
    def convert_ymd_date(s: str):
        ymd_regex = r"^([0-9]{1,4})(-|/)([0-9]{1,2})(-|/)([0-9]{1,2})$"
        return Date._convert_date(ymd_regex, s, [5, 3, 1])

    @staticmethod
    def convert_human_date(s: str):
        # e.g. 14 January 2020
        months = [
            "january", "february", "march", "april", "may",
            "june", "july", "august", "september", "october",
            "november", "december"
        ]

        fields = s.strip().split(" ")
        if len(fields) < 3:
            return None

        day, month, year = tuple(fields[0:3])
        if Date._test_integer(day) and Date._test_integer(year):
            day = int(day)
            year = int(year)
            month = month.lower()
        else:
            return None

        if year > 0:
            if month in months:
                month_idx = months.index(month) + 1
                if 1 <= day <= calendar.monthrange(year, month_idx)[1]:
                    return datetime(year, month_idx, day, 0, 0, tzinfo=timezone.utc)

        return None

    @staticmethod
    def convert_iso8601_date(s: str):       
        try:
            return iso8601.parse_date(s)
        except (iso8601.ParseError, ValueError, OverflowError, TypeError):
            return None
        
    @staticmethod
    def convert_wikidata_date(s: str):
        if s.startswith("+"):
            s = s[1:]
            
        regex = r"\d+\-00\-00T00\:00:00Z"
        search = re.search(regex, s)
        if search is not None:
            tfields = s.split("T")
            
            if len(tfields) != 2:
                return None
            
            d, t = tuple(tfields)            
            fields = d.split("-")
            
            if len(fields) != 3:
                return None
            
            y, m, d = tuple(fields)
            
            good_date = f"{y}-01-01"
            return Date.convert_ymd_date(good_date)
        else: 
            regex2 = r"\d+\-\d+\-\d+T00\:00:00Z" 
            search = re.search(regex2, s)
            if search is not None: 
                tfields = s.split("T") 
                
                if len(tfields) != 2: 
                    return None 
                
                d, t = tuple(tfields) 
                return Date.convert_ymd_date(d) 
            
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
                        return datetime(year, month, day, 0, 0, tzinfo=timezone.utc)

        return None

    @staticmethod
    def _test_integer(i: int):
        try:
            int(i)
        except:
            return False

        return True
