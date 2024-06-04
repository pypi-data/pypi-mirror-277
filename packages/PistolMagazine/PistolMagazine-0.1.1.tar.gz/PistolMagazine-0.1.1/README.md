# PistolMagazine 🎯

PistolMagazine is a data mocking tool designed to help you generate realistic data for testing and development purposes. With support for custom providers and various data types, PistolMagazine makes it easy to simulate real-world data scenarios.

## Features ✨

- **Flexible Data Types** 📊: Supports various data types including integers, floats, strings, timestamps, and more.
- **Custom Providers** 🛠️: Easily create and integrate custom data providers.
- **Extensible** 🚀: Built to be extended with new data types and providers.
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

## Help PistolMagazine

If you find PistolMagazine useful, please ⭐️ Star it at GitHub

[Feature discussions](https://github.com/miyuki-shirogane/PistolMagazine/discussions) and [bug reports](https://github.com/miyuki-shirogane/PistolMagazine/issues) are welcome!

Happy Mocking! 🎉