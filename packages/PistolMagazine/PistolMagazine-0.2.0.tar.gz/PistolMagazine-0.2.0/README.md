# PistolMagazine 🎯
![PyPI - Version](https://img.shields.io/pypi/v/PistolMagazine)


PistolMagazine is a data mocking tool designed to help you generate realistic data for testing and development purposes.

## Features ✨

- **Flexible Data Types** 📊: Supports various data types including integers, floats, strings, timestamps, and more.
- **Custom Providers** 🛠️: Easily create and integrate custom data providers.
- **Random Data Generation** 🎲: Generates realistic random data for testing.

## Installation 📦

Install PistolMagazine using pip:

```bash
pip install pistolmagazine
```

## Quick Start 🚀

Here’s a quick example to get you started:

```python
from pistol_magazine import *
from random import choice

# Define your data structure
data_structure = Dict({
    "id": UInt8(),
    "name": Str(),
    "timestamp": Timestamp(),
    "values": List([Int(), Float()])
})

# Generate mock data
print(data_structure.mock())

# Create a custom provider
@provider
class MyProvider:
    def symbols(self):
        return choice(["BTC", "ETH"])

# Use the custom provider
print(DataMocker.symbols())

```

If you want more detailed instructions, you can refer to the examples and documentation in the [tests' directory](tests).


## Help PistolMagazine

If you find PistolMagazine useful, please ⭐️ Star it at GitHub

[Feature discussions](https://github.com/miyuki-shirogane/PistolMagazine/discussions) and [bug reports](https://github.com/miyuki-shirogane/PistolMagazine/issues) are also welcome!

**Happy Mocking!** 🎉🎉🎉