# Unit 6: Continuous integration - GitHub actions
In unit 4, you will learn about GitHub actions and how to publish a Python package in the Python package index, [PyPi](https://pypi.org/).

When you publish your package, it can be pip installed and then used in ie. jupyter notebooks or more complex software.

Please look [here](PUBLISH.md) for a few notes on how to publish scientific software.

If you run into problems at any point, please contact us via inga.ulusoy@uni-heidelberg.de or [open an issue on github](https://github.com/ssciwr/sustainable_development_course/issues).

The slides for this session are found [here](./unit6_SSD_SSC.pdf). The demonstrations are listed [here](./DEMONSTRATIONS.md) - for unit 6, you can request demonstrations: What would you like to see again? Is there something that you would like to learn more about? The necessary commands for the live lession are listed [here](./STEPS.md).

# 1. Video: Unit 6
Please watch the [video](https://youtu.be/MLzPejUse4Y) to learn about the basics of GitHub actions.

# 2. Try out GitHub actions
Please **fork** [this repository](https://github.com/iulusoy/actions-example-iulusoy) and add a few files to `src` - ie, your custom unittest example that you had come up with in unit 5. Follow through the instructions in the video.

Try out creating branches, opening pull requests and manually triggering the workflow to see when it runs. Look at the output of the runs and try to follow the steps. 

# 3. Publishing a Python package: Optional
Follow the steps in [this tutorial](https://packaging.python.org/tutorials/packaging-projects/) to learn how to publish a python package and what you need to consider (ie., [proper naming](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html) of your package and modules).

# 4. Live lesson
We will meet on Thursday, March 10th at 10:00 AM to 1:00 PM for the live lesson via the previous link. 

During the lesson, we will use [GitHub actions](https://docs.github.com/en/actions) and publish our packages on [TestPyPi](https://test.pypi.org/).

# 5. Asynchronous work in your team
Continue working on your packages and complete the pytest test suite and sphinx documentation, as well as the set-up for GitHub actions. Collaborate through GitHub, and use branches, pull request, and request reviews from your team members before merging any branches into main.

I would ask you to finish your work on this by April 12th. If for some reason you will need more time, please let me know.
