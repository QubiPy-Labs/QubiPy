# setup.py
from setuptools import setup, find_packages

__version__ = '0.2.2'


setup(
    name="QubiPy",
    version=__version__,
    packages=find_packages(),
    install_requires=[],  
    include_package_data=True,
    description="QubiPy, a Python Library for the QUBIC RPC API",
    author="Kyoto",
    author_email="",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
