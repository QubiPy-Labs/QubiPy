# Welcome to the **QubiPy** official documentation, a Python Library for the QUBIC RPC API

!!! note "Beta Version: 0.2.3"
    QubiPy is currently in beta. While functional, some features might change before the stable release.

**QubiPy** is a Python library that provides RPC and Core client functionality. You can interact quickly and easily with the Qubic RPC API using the different methods offered by this library.

## Main Features
* RPC endpoints
* CORE endpoints
* QX endpoints
* Robust core client functionality
* Robust error handling

## Prerequisites
Before installing QubiPy, make sure you have:

* Python 3.10 or higher
* pip (Python package installer)
* Basic knowledge of the [QUBIC API](https://docs.qubic.org/api/rpc/)

!!! note "Version Check"
    You can check your Python version by running:
    ```bash
    python --version
    ```

##  Getting Started

### Installation
!!! tip "Dependencies"
    All dependencies will be installed automatically when you install QubiPy through pip:
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

We welcome all contributions to QubiPy! Whether you want to:

* Fix a bug
* Add a new feature
* Improve documentation
* Submit suggestions

You can learn how to contribute [here](contributing.md)

## Community


!!! tip "Get Help"
    Need help? Join our [Discord community](https://discord.gg/EejFQdQkhG) for quick support and discussions!
