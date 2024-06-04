from datetime import datetime, timedelta
from pistol_magazine.base import _BaseField


class Datetime(_BaseField):
    D_FORMAT_YMD = "%Y-%m-%d %H:%M:%S"
    D_FORMAT_YMD_T = "%Y-%m-%dT%H:%M:%S"

    def __init__(self, date_format=D_FORMAT_YMD, **kwargs):
        self.start = datetime.now()
        self.date_format = date_format
        if not kwargs:
            self.kwargs = {"milliseconds": 1}
        else:
            self.kwargs = kwargs

    def mock(self):
        self.start += timedelta(**self.kwargs)
        return self.start.strftime(self.date_format)

    @classmethod
    def match(cls, value):
        for date_format in cls.defined_list:
            try:
                datetime.strptime(value, date_format)
                return date_format
            except ValueError:
                continue

    def get_datatype(self):
        return "_".join([type(self).__name__, str(self.date_format)])
