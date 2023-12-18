# The required commands in live session 2
## Jupyter notebook in an IDE
Install the extensions: Jupyter; Jupyter Keymap; Jupyter Notebook Renderers.

I also use these relevant extensions additionally, which may be useful to you: GitHub Pull Requests and Issues; Preview; Python; Pylance; YAML

To review notebooks on GitHub, you can use the [reviewnb](https://www.reviewnb.com/) GitHub extension.
## Linting
You run the linter like this:  
```
flake8 your_file.py
```
Or using only `flake8` which will check all the python files in your directory.

For jupyter notebooks, you use flake8-nb to lint the notebooks.
You run this the same way as flake8, either explicitly provide a filename or just run in a directory with your notebooks present.

Now, these will very likely find a lot of styling errors. If you do not want to fix all of these manually, you can use `black` to automatically format your code:
```
black your_file.py
```
You can also run black on your jupyter notebooks. Please note that `black` formats everything in-place, meaning it will directly replace your original file.

## Add linter to pre-commit hooks
You should add the linter and code formatter to your pre-commit hooks. Use the code formatter first and then the linter. The linter will detect syntax errors as well, so even though you reformat your code, you may still get an error for the linter as it detects a "bug". 
The `.pre-commit-config.yaml` file that defines the used pre-commit hooks is found in assignment repo #2.
You need to install and activate the new hooks using `pre-commit install`. 

## PR, code review and merge conflicts
Merge via GitHub or the console following the instructions issued by GitHub.