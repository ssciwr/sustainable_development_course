# The required commands in live session 2
## Jupyter notebook in an IDE
Install the extensions: Jupyter; Jupyter Keymap; Jupyter Notebook Renderers.

I also use these relevant extensions additionally, which may be useful to you: GitHub Pull Requests and Issues; Preview; Python; Pylance; YAML

## Linting
First, install the linter:
```
python -m pip install flake8
```
You then run the linter like this:  
```
flake8 your_file.py
```
Or using only `flake8` which will check all the python files in your directory.

For jupyter notebooks, there is an extension that you can install:
```
python -m pip install flake8-nb
```
You run this the same way as flake8, either explicitly provide a filename or just run in a directory with your notebooks present.

Now, these will very likely find a lot of styling errors. If you do not want to fix all of these manually, you can use `black` to automatically format your code:
```
python -m pip install black
```
You run it like so:
```
black your_file.py
```
Again, there is an extension for jupyter notebooks:
```
python -m pip install black[jupyter]
```
Run using `black` on your notebook file.

## Add linter to pre-commit hooks
You should add the linter and code formatter to your pre-commit hooks. Use the code formatter first and then the linter. The linter will detect syntax errors as well, so even though you reformat your code, you may still get an error for the linter as it detects a "bug". 

For `black`, you need to add the following lines to your `.pre-commit-config.yaml`:
```
  - repo: https://github.com/psf/black
    rev: 21.11b0
    hooks:
    - id: black
```
To reformat notebooks with `black`:
```
  - repo: https://github.com/dfm/black_nbconvert
    rev: v0.3.0
    hooks:
      - id: black_nbconvert
```
For `flake8`: 
```
  -   repo: https://github.com/pycqa/flake8
      rev: 4.0.1 
      hooks:
      -   id: flake8
```
For flake8-nb:
```
  -   repo: https://github.com/s-weigand/flake8-nb
      rev: v0.3.1 
      hooks:
      -   id: flake8-nb
```
You need to install the new hooks using `pre-commit install`. I suggest you do this one by one to check everything is running correctly.

## Performance of code
You can check the performance of code using the `time` module, as demonstrated in the [preparation/test_install.py] script. To get more advanced profiling, use cProfile as this:
```
python -m cProfile -o temp.dat your-script.py
```
Visualize the output using snakeviz:
```
python -m pip install snakeviz
snakeviz temp.dat
```
## PR, code review and merge conflicts
Merge via GitHub or the console following the instructions issued by GitHub.