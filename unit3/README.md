# Unit 3: Testing, testing, testing ... and writing good documentation
In unit 3, you will learn about types of tests, and implement unit tests for your developed python module. We will also continue to work on the documentation and publish it on [readthedocs](https://readthedocs.org/).

If you run into problems at any point, please contact us via inga.ulusoy@uni-heidelberg.de or [open an issue on github](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue).

# 1. Video: Unit 3, Part 1
Please watch the [video](https://youtu.be/11t1EGV3V3I) to learn about the importance of software testing, types of software tests, test-driven development and the unittest module.

# 2. Write your own unit test in the unittest framework
Write an example function in python that is to be tested using unittest and different assert methods, as explained in the video. Try what happens if your test fails.

# 3. Video: Unit 2, Part 2
Please watch the [video](https://youtu.be/eSIygwMcK24) - you will learn about pytest unit tests and what to include in a good documentation.

# 4. Quiz
Answer the [questions](https://forms.gle/FpACFFcesq5vZB7D6) (this is strictly anonymous).

# 5. Preparation for the live lesson
There are a few items that you will need to address before the live session. One of the team members should take a lead in this, ideally the repository owner.
- if your documentation folder is called `doc` and not `docs`: include the line `doc/_build/` in your `.gitignore` file
- if you would like GitHub to correctly recognize the languages that you are using in your repository: add a `.gitattributes` file according to the [example repository](https://github.com/ssciwr/sustainable_development_course) with the content
```
# correct the language detection on github
# exclude data files from linguist analysis
data/* linguist-generated
```
where you replace `data/` with the folder containing the data files that are read in by your package.
- add a file `requirements.txt` that contains the required libraries for your package to run (see the [example repository](https://github.com/ssciwr/sustainable_development_course))
- potentially update the sphinx module files, if you have added further modules in your `source/package` directory (`sphinx-apidoc` or compare to the [example repository](https://github.com/ssciwr/sustainable_development_course))
- Prepare a user account on [readthedocs](https://readthedocs.org/) (this has to be done by the repository owner). You can already try to publish your documentation on RTD; compare to the [documentation of the example repository](https://team0.readthedocs.io/en/latest/index.html)

# 6. Live lesson
We will meet on Thursday, March 25th at 12:30 - 3:00 PM for the live lesson via the previous link. In addition to that, I have sent you a [youtube link](https://youtu.be/ep9vSsVI26s) for live streaming - please keep both open during the session.

During the lesson, we will use [pytest](https://docs.pytest.org/en/stable/), [recommonmark](https://recommonmark.readthedocs.io/en/latest/), and [napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html).

# 7. Asynchronous work in your team
Continue working on your module(s) during the week and complete the pytest test suite and documentation. Collaborate through GitHub, and use branches, pull request, and request reviews from your team members before merging any branches into main.

# 7. Evaluation of unit 3
This is not mandatory, but we would highly appreciate your feedback. Please help us by [answering a couple of questions](https://forms.gle/FoCgR6ZDLC8gjkxB7).
