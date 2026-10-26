# Python Driver for Sensirion Mass Flow Controllers/Meters

This package contains the SHDLC driver for the `Sensirion SFC5xxx`_ mass flow
controllers and `Sensirion SFM5xxx`_ mass flow meters which have an RS485
interface using the SHDLC protocol. MFCs and MFMs which do not have an SHDLC
interface are not supported by this driver.

The driver provides all SHDLC commands (e.g. set setpoint and read measured
flow) as Python methods and handles all the low-level things like type
conversions, checksum calculation, error handling etc.

## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-shdlc-sfc5xxx) for an API description and a
[quickstart](https://sensirion.github.io/python-shdlc-sfc5xxx/execute-measurements.html) example.
https://sensirion.github.io/python-shdlc-sfc5xxx/.


## Contributing

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `main` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :-)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

## License

See [LICENSE](LICENSE).
