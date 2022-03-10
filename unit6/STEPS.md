# The required commands in live session 6

## Publishing your Python package
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
name = myteam
version = 0.0.1
author = Inga Ulusoy
author_email = inga.ulusoy@uni-heidelberg.de
description = team0 data analysis package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/iulusoy/my-test-repo
project_urls =
    Bug Tracker = https://github.com/iulusoy/my-test-repo/issues
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
python -m pip install --upgrade build
python -m pip install --user --upgrade twine
```
- Build your package in the base directory
```
python3 -m build
```
- Create a new token on [TestPyPi](https://test.pypi.org/manage/account/#api-tokens) with no limited scope - save this somewhere, you need it for publishing the package and you will not see this again.
- upload your package to TestPyPi
```
twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
```
It will ask you for a username and password, you need to provide `__token__` as username, and your token as password, so
```
username = __token__
password = pypi-yourtokengoeshere
```
- Install your new package (replace the URL with your package URL):
```
python -m pip install -i https://test.pypi.org/simple/ myteam
```
or
```
python -m pip install -i https://test.pypi.org/simple/ myteam -U
```
if you want to upgrade to a new version.
- Open a python terminal and try to import your package
```
python
import myteam
```
- Try to load your package into a jupyter notebook. 
