from setuptools import setup, find_packages

__version__ = '0.4.1'


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    'requests>=2.32.3',
    'urllib3>=2.2.3',
]

setup(
    name="QubiPy",
    version=__version__,
    packages=find_packages(exclude=['tests*', 'tests.*', 'docs*', 'docs.*']),
    package_data={
        'qubipy.crypto': ['*.dll', '*.dylib', '*.so'],
    },
    install_requires=install_requires,
    include_package_data=True,
    description="QubiPy, a Python Library for the QUBIC RPC API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kyoto",
    author_email="qubipy.labs@gmail.com",
    url="https://github.com/QubiPy-Labs/QubiPy",
    project_urls={
        "Documentation": "https://qubipy.readthedocs.io",
        "Source Code": "https://github.com/QubiPy-Labs/QubiPy",
        "Bug Tracker": "https://github.com/QubiPy-Labs/QubiPy/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
    ],
    python_requires=">=3.10",
    keywords="qubic, blockchain, rpc, api, cryptocurrency",
)