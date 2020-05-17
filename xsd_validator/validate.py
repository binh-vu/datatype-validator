import os

from xsd_validator.datatypes import boolean, integer, isbn, real, date, email, url, geocoord, string

_datatypes_list = [
    boolean.Boolean,
    email.Email,
    url.Url,
    integer.Integer,
    isbn.ISBN,
    real.Real,
    date.Date,
    geocoord.Geocoord,
]

def get_datatype(field: str):
    for dt in _datatypes_list:
        converter = dt(field)
        valid = converter.is_valid()
        if valid:
            return converter

    return string.String(field)


"""
def main():
    p = "/home/andrea/Download/Tables_Round1/tables/"
    dirs = os.listdir(p)
    res = set()
    for filename in dirs:
        fullpath = os.path.join(p, filename)
        with open(fullpath) as f:
            for line in f:
                fields = [
                    item.strip()
                    for item in line.split(",")
                ]
                for field in fields:
                    datatype = get_datatype(field)
                    res.add((datatype.to_python(), type(datatype).__name__))

    res = list(res)
    res = sorted(res, key=lambda item: item[1])
    for r in res:
        print(r[0], "|", r[1])
"""                   


if __name__ == '__main__':
    main()