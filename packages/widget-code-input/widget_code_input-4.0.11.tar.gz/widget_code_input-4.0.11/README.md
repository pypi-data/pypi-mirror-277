
# widget-code-input


[![PyPI version](https://badge.fury.io/py/widget-code-input.svg)](https://badge.fury.io/py/widget-code-input)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/osscar-org/widget-code-input/main?labpath=%2Fexamples%2FWidget_Demo.ipynb)

A widget to allow input of a python function, with syntax highlighting.


## Installation

You can install using `pip`:

```bash
pip install widget_code_input
```

### Releasing and publishing a new version

In order to make a new release of the library and publish to PYPI, run

```bash
bumpver update --major/--minor/--patch
```

This will

- update version numbers, make a corresponding `git commit` and a `git tag`;
- push this commit and tag to Github, which triggers the Github Action that makes a new Github Release and publishes the package to PYPI.


## Acknowledgements

We acknowledge support from the EPFL Open Science Fund via the [OSSCAR](http://www.osscar.org) project.

<img src='https://www.osscar.org/_images/logos.png' width='700'>
