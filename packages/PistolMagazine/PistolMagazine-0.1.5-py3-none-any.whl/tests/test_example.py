from pprint import pprint
import pytest
from pistol_magazine import *
from random import choice

a = Int()


def test_e():
    print(a.name_map.values())


def test():
    c = Dict(
        {
            "a": UInt(),
            "b": Timestamp(),
            "C": List(
                [
                    Datetime(Datetime.D_FORMAT_YMD),
                    Float()
                ]
            )
        }
    )
    print(c.mock())


@pytest.mark.parametrize("t", a.name_map.values())
def test2(t):
    t_instance = t()
    print(t_instance.mock())
    assert t_instance.mock()


def test3():
    c = Int()
    b = Float()
    print(c.fake.word())
    print(c.fake == b.fake)
    print(a.name_map == b.name_map)


def test_dict():
    c = Dict({"a": UInt8(), "b": Str(), "c": Timestamp(), "d": List()})
    print(c.mock())
    b = Dict()
    print(b.mock())


def test4():
    d = DataMocker()
    assert d.models
    assert not d.mock()


def test_data_mocker():
    class PositionMocker(DataMocker):
        symbol: Str
        x: Float
        update_at: Timestamp = Timestamp(Timestamp.D_TIMEE13)

    data = PositionMocker().mock()
    print(data)
    print(data["symbol"])
    print(data["update_at"])


models = {
    'a': {'1': 'Datetime_%Y-%m-%dT%H:%M:%S', '2': 'StrFloat', '3': 'Float', '4': 'Int'},
    'b': 'Timestamp_0', 'c': 'Timestamp_3', 'd': 'Str',
    'e': ['StrTimestamp_3', 'Str', {'f': 'Int', "g": "StrInt"}]
}


def test_str_timestamp():
    print(StrTimestamp.match("1716964369839"))
    print(Float(left=2, right=7).mock())


def test_read_model_from_dicts():
    # Given a data sample, return format model
    data = {
        "a": {
            "1": "2022-01-01T00:00:00",
            "2": "20.22",
            "3": 20.22,
            "4": 100,
        },
        "b": 1680441525,
        "c": 1680441525000,
        "d": "i am strong",
        "e": ["1680441525000000", "2022-01-01T00:00:001",
              {
                  "f": 1000,
                  "g": "10000"
              }]
    }
    data_mocker = DataMocker.read_models_from_dicts(data)
    pprint(data_mocker.get_datatype())


def test_load_dicts():
    # Define a format model to generate detailed data
    m = DataMocker.load_models_from_dict(models)
    pprint(m.mock())


@provider
class MyProvider:
    def symbols(self):
        return choice(["BTC", "ETH"])

    def x(self):
        return choice(["1", "2", "3"])


def test_pro():
    print(DataMocker().symbols())


def test_x():
    print(StrTimestamp.match("1680441525000000"))
