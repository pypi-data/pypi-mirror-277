from pprint import pprint
from random import choice
from pistol_magazine import DataMocker, provider


def test_read_model_from_dicts():
    # Given a data sample, return format model
    """
    :return: e.g.
    {'a': {'1': 'Datetime_%Y-%m-%dT%H:%M:%S',
           '2': 'StrFloat',
           '3': 'Float',
           '4': 'Int'},
     'b': 'Timestamp_0',
     'c': 'Timestamp_3',
     'd': 'Str',
     'e': ['StrInt', 'Str', {'f': 'Int', 'g': 'StrInt'}]}
    """
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
    """
    :return: e.g.
    {'a': {'1': '2024-06-05T16:49:56',
           '2': '40.48',
           '3': 63.33,
           '4': 2097091821547551986},
     'b': 1717577396,
     'c': 1717577396917,
     'd': 'model',
     'e': ['1717577396917',
           'friend',
           {'f': -6276567609125728972, 'g': '-5731993852980988010'}]}
    """
    models = {
        'a': {'1': 'Datetime_%Y-%m-%dT%H:%M:%S', '2': 'StrFloat', '3': 'Float', '4': 'Int'},
        'b': 'Timestamp_0', 'c': 'Timestamp_3', 'd': 'Str',
        'e': ['StrTimestamp_3', 'Str', {'f': 'Int', "g": "StrInt"}]
    }
    m = DataMocker.load_models_from_dict(models)
    pprint(m.mock())


@provider
class MyProvider:
    def symbols(self):
        return choice(["BTC", "ETH"])


def test_provider():
    print(DataMocker().symbols())  # e.g. "BTC"



