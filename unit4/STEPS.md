# The required commands in live session 4
extensions = ['sphinx.ext.autodoc',
              'recommonmark',
              'sphinx.ext.napoleon'
]
```
Include `modules` in `index.rst`.

There are a few items that you will need to address before the live session. One of the team members should take a lead in this, ideally the repository owner.
- if your documentation folder is called `doc` and not `docs`: include the line `doc/_build/` in your `.gitignore` file
- if you would like GitHub to correctly recognize the languages that you are using in your repository: add a `.gitattributes` file according to the [example repository](https://github.com/iulusoy/team0) with the content
```
# correct the language detection on github
# exclude data files from linguist analysis
data/* linguist-generated
```
where you replace `data/` with the folder containing the data files that are read in by your package.
- add a file `requirements.txt` that contains the required libraries for your package to run (see the [example repository](https://github.com/iulusoy/team0))
- potentially update the sphinx module files, if you have added further modules in your `source/package` directory (`sphinx-apidoc` or compare to the [example repository](https://github.com/iulusoy/team0))
- Prepare a user account on [readthedocs](https://readthedocs.org/) (this has to be done by the repository owner). You can already try to publish your documentation on RTD; compare to the [documentation of the example repository](https://team0.readthedocs.io/en/latest/index.html)