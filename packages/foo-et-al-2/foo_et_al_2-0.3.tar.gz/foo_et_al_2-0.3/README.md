[![PyPI - Version](https://img.shields.io/pypi/v/foo_et_al_2)](https://pypi.org/project/foo-et-al-2/)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Joseph-Willem-Ricci/foo_et_al_2)
![GitHub top language](https://img.shields.io/github/languages/top/Joseph-Willem-Ricci/foo_et_al_2)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Joseph-Willem-Ricci/foo_et_al_2/.github%2Fworkflows%2Fci.yml)


# FOO (ET AL)^2
## UCAR Science Feature Toolkit

Foo (Et Al)^2 is a package for calculating the complex Foo et al. parameterization, proposed in 2024 by UCAR researchers Foo, Bar and Baz. In the spirit of open science and scientific progress, we extend an open invitation to contribute new science features alongside the Foo et al. parameterization, making this package Foo et al., et al.; Foo (Et Al)^2

# Contribution Guidelines

## File Strucutre

`foo_et_al_2/foo_et_al` contains files for the core Foo et al. parameterization feature.

`foo_et_al_2/et_al` is the directory for new science feature contributions.

## Code Style
For ease of communication and maintenence, please conform to the PEP 8 Style Guide.

## General Contribution Version Control Guidelines
1. Create and checkout a new working branch from `dev` in the GitHub repository
2. Contribute new features or suggest changes to existing features
3. In your terminal, run `python tests/run_tests.py` to test your contribution along with pre-existing tests
4. Add or edit documentation in docs/api.md if necessary
5. Commit your changes to the new branch
6. Open a pull request, merging into `dev` with a description of the change, and request review from a maintainer

### If Contributing New Science Features
1. Create a new package in `foo_et_al_2/et_al` with a descriptive name, say `/_example_contribution`
2. Create your new python files, say `hello_world.py` and `is_palindrome.py` within `/_example_contribution`
3. In `foo_et_al_2/tests` create a test file in the format `test_<new_package_name>.py` with unit tests for all files in your new package

See example contribution files in the file tree.

### If Suggesting Changes to Existing Features

See "Merge Pull Request #1" in GitHub for an example of a successful feature change suggestion.


# Documentation
Read the documentation [here](docs/index.md).

# Installation Instructions
To install the Foo (Et Al)^2 software package, run the following command in your terminal:

`pip install foo-et-al-2`

You can view the project on the Python Package Index at https://pypi.org/project/foo-et-al-2/

# Usage Examples
Once installed, methods from the package can be used, as seen in the following examples:

```py
from foo_et_al.foo_et_al import foo_et_al_param
bar = 1
baz = foo_et_al_param(bar)
```

```py
from et_al._example_contribution.is_palindrome import is_palindrome
print(is_palindrome("racecar"))
print(is_palindrome("UCAR"))
```

Expected output:
```
True
False
```


# Discussion Forum
Please join the Foo (Et Al)^2 community in the [discussion forum](https://groups.google.com/g/foo_et_al_2).

# GitHub
The GitHub repository is [avaialble here](https://github.com/Joseph-Willem-Ricci/foo_et_al_2)

# Citing FOO (ET AL)^2

If you use this software, please cite it as

`FBB Lab. (2024). UCAR Science Feature Toolkit: Foo (Et Al)^2.`