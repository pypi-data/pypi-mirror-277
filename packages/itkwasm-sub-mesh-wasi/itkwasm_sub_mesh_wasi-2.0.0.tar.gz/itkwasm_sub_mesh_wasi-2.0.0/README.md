# itkwasm-sub-mesh-wasi

[![PyPI version](https://badge.fury.io/py/itkwasm-sub-mesh-wasi.svg)](https://badge.fury.io/py/itkwasm-sub-mesh-wasi)

Extract a subset of a mesh given by the cell identifiers. WASI implementation.

This package provides the WASI WebAssembly implementation. It is usually not called directly. Please use [`itkwasm-sub-mesh`](https://pypi.org/project/itkwasm-sub-mesh/) instead.


## Installation

```sh
pip install itkwasm-sub-mesh-wasi
```

## Development

```sh
pip install pytest
pip install -e .
pytest

# or
pip install hatch
hatch run test
```
