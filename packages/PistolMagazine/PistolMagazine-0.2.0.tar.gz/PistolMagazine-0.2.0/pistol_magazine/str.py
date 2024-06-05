from pistol_magazine.base import _BaseField
from datetime import datetime


class Str(_BaseField):

    def mock(self):
        return self.fake.word()

    @classmethod
    def match(cls, value: str):
        if value.isdigit():
            return StrInt()
        else:
            try:
                float(value)
                return StrFloat()
            except ValueError:
                return Str()


class StrInt(_BaseField):

    def __init__(self, byte_nums=64, unsigned=False):
        self.byte_nums = byte_nums
        self.unsigned = unsigned
        if unsigned:
            min_num = 0
            max_num = 2 ** byte_nums - 1
        else:
            min_num = -2 ** (byte_nums - 1)
            max_num = 2 ** (byte_nums - 1) - 1
        self.args = [min_num, max_num]

    def mock(self):
        from pistol_magazine.int import Int
        int_instance = Int(self.byte_nums, self.unsigned)
        return str(int_instance.mock())


class StrFloat(_BaseField):
    def __init__(self, left=2, right=2, unsigned=False):
        self.left = int(left)
        self.right = int(right)
        self.unsigned = unsigned

    def mock(self):
        from pistol_magazine.float import Float
        float_instance = Float(self.left, self.right, self.unsigned)
        return str(float_instance.mock())

    def get_datatype(self):
        return type(self).__name__


class StrTimestamp(_BaseField):
    D_TIMEE13 = 3
    D_TIMEE10 = 0

    def __init__(self, times: int or str = D_TIMEE13, **kwargs):
        self.current_time = datetime.now()
        self.times = int(times)
        self.kwargs = kwargs

    def mock(self):
        from pistol_magazine import Timestamp
        return str(Timestamp(self.times, **self.kwargs).mock())

    @classmethod
    def match(cls, value: str):
        if value.isdigit():
            from pistol_magazine import Timestamp
            result = Timestamp.match(int(value))
            return result
