# piplink

piplink is a Python package for uploading packages to PyPI.

## Installation

You can install piplink using pip:

`pip install piplink`

## Usage

After installing piplink, you can use the command line interface `piplink` to upload your Python packages to PyPI.

`piplink`

### Uploading Packages

Before using `piplink`, make sure you have `setuptools` and `wheel` installed. If not, you can install them using:

`pip install setuptools wheel`

To upload your package, you can follow these steps:

1. Create distributions using setuptools:

`python setup.py sdist bdist_wheel`

2. Upload your package using piplink:

`piplink`

## Requirements

- Python 3.6 and above
- requests
- requests-toolbelt

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for using piplink! 🚀
