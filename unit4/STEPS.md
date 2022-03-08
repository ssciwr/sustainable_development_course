# The required commands in live session 4

## Sphinx
Install sphinx using  
`python -m pip install sphinx`  
and extensions via  
```
python -m pip install myst-parser
python -m pip install sphinxcontrib-napoleon
```
Now set up the documentation folder and initialize sphinx:
```
mkdir docs
cd docs/
sphinx-quickstart
```
Typoe `y`, the name of your project, the author names, the project release (ie. 0.1), language `en`.

Open `conf.py` and uncomment
```
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
```
Replace `sys.path.insert(0, os.path.abspath('.'))` with the path to your package (modules), in my example `sys.path.insert(0, os.path.abspath('../src/'))`.
Activate further extensions through
```
extensions = ['sphinx.ext.autodoc',
              'recommonmark',
              'sphinx.ext.napoleon'
]
```
in your `conf.py`.

Now you can quickstart the autobuild of the sphinx documentation:  
`sphinx-apidoc -o source/ ../src/` 
This is a step that often leads to problems later on, so if things don't work out for you let me know and I will take a look. The outcome is unfortunately platform-dependent. 

Type `make html` and you should then find a `index.html` file in your `docs/_build/html/` directory that you can preview using the VSCode HTML preview extension or by opening it from the file menu (opens the browser).

It should contain the name of your package, the author name and Index/Module index. Your modules should be linked here.

Very likely `make html` will return an error:
```
checking consistency... /home/inga/teaching/SSD_March2022/demos/unit1/my-test-repo/docs/source/modules.rst: WARNING: document isn't included in any toctree
```
You can add `modules` into the `index.rst` file to remedy this. But it will work either way.

It is possible that your modules will not be linked correctly. If so, we need to edit the `modules.rst` file or the respective module files in the source directory. Let me know and I will show you how.

## Include markdown in your sphinx documentation

Include `readme` in `index.rst` and any other files (`license`, `installation`, etc). Place readme.md and installation.md, etc, files in your `docs/source/` folder to include them in the documentation.

## requirements.txt
Add a file `requirements.txt` that contains the required libraries for your package to run (see the [example repository](https://github.com/iulusoy/my-test-repo)).

## Add your repo to readthedocs
Import your repo into readthedocs to have it publicly hosted.

## Use GitHub pages
Use GitHub pages to host your documentation
