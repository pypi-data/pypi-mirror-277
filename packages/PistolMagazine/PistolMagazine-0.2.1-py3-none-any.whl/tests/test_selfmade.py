from pprint import pprint
from random import choice
from pistol_magazine import DataMocker, provider


def test_model_data_conversion():
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
    models = {
        'a': {'1': 'Datetime_%Y-%m-%dT%H:%M:%S', '2': 'StrFloat', '3': 'Float', '4': 'Int'},
        'b': 'Timestamp_0', 'c': 'Timestamp_3', 'd': 'Str',
        'e': ['StrTimestamp_3', 'Str', {'f': 'Int', "g": "StrInt"}]
    }
    data_mocker1 = DataMocker.data_to_model(data)
    data_mocker2 = DataMocker.model_to_data(models)
    # Input raw data ---------> Data format
    pprint(data_mocker1.get_datatype())
    # Input raw data ---------> New mock data in the same format
    pprint(data_mocker1.mock())
    # Input model data ---------> Mock data in the given format
    pprint(data_mocker2.mock())


@provider
class MyProvider:
    def symbols(self):
        return choice(["BTC", "ETH"])


def test_provider():
    print(DataMocker().symbols())  # e.g. "BTC"



