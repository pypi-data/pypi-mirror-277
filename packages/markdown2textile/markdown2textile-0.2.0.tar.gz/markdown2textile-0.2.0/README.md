# markdown2textile

[![PyPI - Version](https://img.shields.io/pypi/v/markdown2textile.svg)](https://pypi.org/project/markdown2textile)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/markdown2textile.svg)](https://pypi.org/project/markdown2textile)

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install markdown2textile
```

## Usage

This `markdown2textile` command-line utility converts a markdown file to a textile file or vice versa.

If `i` `-input` receives file extension `.md` or `.markdown`, it will convert the markdown file to textile file.
otherwise, it will convert the textile file to markdown file.

```plaintext
Usage: markdown2textile [OPTIONS]

Options:
  --version              Show the version and exit.
  -i, --input FILENAME   The input file. Default is stdin.
  -o, --output FILENAME  The output file. Default is stdout.
  -h, --help             Show this message and exit.
```

## License

`markdown2textile` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
