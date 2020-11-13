# Python Driver for Sensirion Mass Flow Controllers/Meters

This repository contains the SHDLC driver for the Sensirion SFC5xxx MFCs and
SFM5xxx MFMs as a Python package. For details, please read the package
description in [README.rst](README.rst).

## Usage

See package description in [README.rst](README.rst) and user manual at
https://sensirion.github.io/python-shdlc-sfc5xxx/.

## Development

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

### Run tests

Unit tests can be run with [`pytest`](https://pytest.org/):

```bash
pip install -e .[test]          # Install requirements
pytest -m "not needs_device"    # Run tests without hardware
pytest                          # Run all tests
```

The tests with the marker `needs_device` have following requirements:

- An SFC5xxx device must be connected to the computer.
  - *NOTE: Firmware version must be 1.66 or higher.*
  - **WARNING: Some tests modify non-volatile configurations of the MFC, restore
    factory defaults etc.! Do not run the tests on a device which you don't
    want to get modified!**
- You have to specify the serial port (and optionally other connection
  parameters) used to connect to the SFC5xxx device:
  - `--serial-port`: The serial port where the device is connected
    (e.g. `COM7`).
  - `--serial-bitrate`: The bitrate of the connected device (defaults to
    `115200`).
  - `--slave-address`: The slave address of the connected device (defaults to
    `0`).


### Build documentation

The documentation can be built with [Sphinx](http://www.sphinx-doc.org/):

```bash
python setup.py install                        # Install package
pip install -r docs/requirements.txt           # Install requirements
sphinx-versioning build docs docs/_build/html  # Build documentation
```

## License

See [LICENSE](LICENSE).
