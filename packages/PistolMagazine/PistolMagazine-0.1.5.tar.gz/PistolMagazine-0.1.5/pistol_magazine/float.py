from pistol_magazine.base import _BaseField


class Float(_BaseField):
    def __init__(self, left=2, right=2):
        self.left = int(left)
        self.right = int(right)

    def mock(self):
        return self.fake.pyfloat(self.left, self.right)

    def get_datatype(self):
        return type(self).__name__
        # return "_".join([type(self).__name__, str(self.left), str(self.right)])
