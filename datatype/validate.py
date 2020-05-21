import os

from .validators import boolean, integer, isbn, real, date, email, url, geocoord, string

_datatypes_list = [
    boolean.Boolean,
    email.Email,
    url.Url,
    integer.Integer,
    isbn.ISBN,
    real.Real,
    date.Date,
    geocoord.Geocoord,
    string.String
]

def get_datatype(field: str):
    for dt in _datatypes_list:
        converter = dt(field)
        valid = converter.is_valid()
        if valid:
            return converter

    return string.Unknown(field)