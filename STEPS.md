# Unit 2
pip install sphinx
sphinx-apidoc -o ./source/. ../src/
add your source files to source/index.rst
make sure when adding comments to use the correct indent
to run unittest: python -m unittest

# Unit 3
## pytest
- create `__init__.py` in your package directory
- create `conftest.py` in your package directory
- create a `test` directory

## Documentation
- Add into your `conf.py`:
```
extensions = ['sphinx.ext.autodoc',
              'recommonmark',
              'sphinx.ext.napoleon'
]
```
and
```
html_theme = 'default'
```
- Add into your `index.rst`:
```
readme
installation
license
help
modules
```
- Generate markdown files `readme.md`, `installation.md`, etc in your `doc/source` directory (the ones that are missing in the previous step)
- Fill these files with content; add further files as you see fit
- Compile your documentation on your local computer and check that it works
- Add your documentation to readthedocs

# Unit 4

## Publish your package
- fill __init__.py with content:
```
from .modulename import functionname
from .modulename import classname
```
include # noqa: F401 after each line so that `flake8` will not complain about unused module imports
- create `pyproject.toml`
```
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
```
- add `setup.cfg` file in your base directory
```
[metadata]
name = team0-iulusoy
version = 0.0.1
author = Inga Ulusoy
author_email = inga.ulusoy@uni-heidelberg.de
description = team0 data analysis package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/iulusoy/team0
project_urls =
    Bug Tracker = https://github.com/iulusoy/team0/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent
[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6
[options.packages.find]
where = src
```
replace the relevant metadata with your own specifics
- upgrade required build tools:
```
python3 -m pip install --upgrade build
python3 -m pip install --user --upgrade twine
```
- Create a new token on [TestPyPi](https://test.pypi.org/manage/account/#api-tokens) with no limited scope - save this somewhere, you need it for publishing the package and you will not see this again - you can create a .pypirc file **in your home directory** with the content:
```
  [testpypi]
  username = __token__
  password = pypi-yourtokengoeshere
```
Set the permission so that other users cannot access this file `chmod 600 ~/.pypirc`.
- Build your package in the base directory
```
python3 -m build
```
- upload your repo to TestPyPi
```
twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
```
- Install your new package (replace the URL with your package URL):
```
python -m pip install -i https://test.pypi.org/simple/ team0
```
or
```
python -m pip install -i https://test.pypi.org/simple/ team0 -U
```
if you want to upgrade to a new version.
- Open a python terminal and try to import your package
```
python
import team0iu as t0
```
- Try to load your package into a jupyter notebook 
