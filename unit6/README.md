# Unit 6: Continuous integration - GitHub actions
In unit 4, you will learn about GitHub actions and how to publish a Python package in the Python package index, [PyPi](https://pypi.org/).

When you publish your package, it can be pip installed and then used in ie. jupyter notebooks or more complex software.

Please look [here](PUBLISH.md) for a few notes on how to publish scientific software.

If you run into problems at any point, please contact us via inga.ulusoy@uni-heidelberg.de or [open an issue on github](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue).

# 1. Video: Unit 6, part 1
Please watch the [video]() to learn about the basics of GitHub actions.

# 2. Try out GitHub actions
Please **fork** [this repository](https://github.com/iulusoy/actions-example-iulusoy) and add a few files to `src` - ie, your custom unittest example that you had come up with in unit 5. Try out creating branches, opening pull requests and manually triggering the workflow to see when it runs. Look at the output of the runs and try to follow the steps. 

# 3. Video: Unit 6, part 2
Please watch the [video]() to learn how to run the linter and unit tests automatically through GitHub actions, and how your documentation can automatically be updated on readthedocs/GitHub pages.

# 4. Tutorial for publishing Python packages
Follow the steps in [this tutorial](https://packaging.python.org/tutorials/packaging-projects/) to learn how to publish a python package and what you need to consider (ie., [proper naming](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html) of your package and modules).

# 5. Live lesson
We will meet on Thursday, March 10th at 10:00 AM to 1:00 PM for the live lesson via the previous link. 

During the lesson, we will use [GitHub actions](https://docs.github.com/en/actions), publish our documentation on [readthedocs](https://readthedocs.org/) and publish our packages on [TestPyPi](https://test.pypi.org/).

# 6. Asynchronous work in your team
Continue working on your packages and complete the pytest test suite and sphinx documentation, as well as the set-up for GitHub actions. Collaborate through GitHub, and use branches, pull request, and request reviews from your team members before merging any branches into main.

I would ask you to finish your work on this by April 12th. If for some reason you will need more time, please let me know.
