# Welcome to the **QubiPy** official documentation, a Python Library for the QUBIC RPC API

**QubiPy** is a Python library that provides RPC and Core client functionality. You can interact quickly and easily with the Qubic RPC API using the different methods offered by this library.

## Main Features
* RPC endpoints
* CORE endpoints
* QX endpoints
* Robust core client functionality
* Robust error handling

## Getting Started

### Installation
To install QubiPy, run:

```bash
pip install qubipy
```

## Basic example

Let's see some basic examples of the use of the library.

### Get the latest tick
Here's a simple example of how to use QubiPy. For example, If you want to get the latest tick from the RPC server :

```python
from qubipy.rpc import rpc_client

RPC = QubiPy_RPC()
tick = RPC.get_latest_tick()

print(f"Tick: {tick}")

# 17650910
```

To see more advanced examples, please visit [Advances examples](examples.md)

## Contributing
We welcome contributions! Check out our GitHub repository for:

* Source code
* Issue tracking
* Pull requests
* Development guidelines
