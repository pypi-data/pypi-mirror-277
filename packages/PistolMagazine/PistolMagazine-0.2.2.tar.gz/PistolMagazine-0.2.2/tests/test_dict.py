from pistol_magazine import List, Datetime, Float, Timestamp, Dict, StrInt


def test_dict():
    dict = Dict()
    # Default {'a': int, 'b': str, 'c': timestamp}, e.g. {'a': 5047713556328115783, 'b': 'last', 'c': 1717576783610}
    print(dict.mock())

    expect_format = {
        "a": Float(left=2, right=4, unsigned=True),
        "b": Timestamp(Timestamp.D_TIMEE10, days=2),
        "C": List(
            [
                Datetime(Datetime.D_FORMAT_YMD_T, weeks=2),
                StrInt(byte_nums=6, unsigned=True)
            ]
        )
    }
    print(Dict(expect_format).mock())  # e.g. {'a': -54.9438, 'b': 1717673498, 'C': ['2024-06-15T04:50:46', '5']}
