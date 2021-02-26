# Unit 1: Introduction to git

In unit 1, you will learn and practice the git basics. Before we start, there are a few items that you will need to work through, to ensure your computer is set up with everything we need for the course.

If you run into problems at any point, please contact us via inga.ulusoy@uni-heidelberg.de or [open an issue on github](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue).

# 1. Prepare for the lesson
## Windows users
### Option A
1. Please install the Ubuntu Subsystem (Windows Subsystem for Linux) following the steps detailed [here](https://www.windowscentral.com/install-windows-subsystem-linux-windows-10).
2. Open a terminal (launch the Ubuntu terminal).
3. Update/upgrade the pre-installed libraries through  
`sudo apt update`  
`sudo apt upgrade`  
3. Install git  
`sudo apt install git-all`
4. Install python/jupyter/numpy/pandas/seaborn using the installation script.

### Option B
1. Install git support for your favorite IDE, for example [Visual Studio Code](https://visualstudio.microsoft.com/downloads/) and make sure that it works with github.
2. Make sure that you have a git and a python environment set up and python language support/linter installed.

## Mac users
1. Install Xcode command line tools

## Linux users
1. Install git  
`sudo apt install git-all`

## All participants:  
1. In your terminal, you need to provide your name and email for your first-time git usage:  
```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```
2. Please download the install script in the github repository, from [here](https://github.com/ssciwr/sustainable_development_course/blob/main/downloads/test_install.py) (right-click on the link and select "save file as"/"save link as" to download the file). This will check all the libraries.
3. Move the script to your current folder in the terminal and type  
`python test_install.py` or run it in your IDE. Two windows with graphs should pop up, the first one saying "testing matplotlib", the second one "testing seaborn", both of them showing a straight line. The output of the script should approximately read  
```
Testing pandas  
   a  b  c  
0  1  2  3  
1  4  5  6  
The script took 2.1 seconds to run!
```
4. It is recommended to use an IDE (Integrated Development Environment). If you do not have one already, [Visual Studio Code](https://visualstudio.microsoft.com/downloads/) is recommended for Windows; [Atom](https://atom.io/) for Linux users, but should also work on Windows or Mac OS. If you have never used an IDE before, you will need to install a couple of additional packages within the editor, such as python language support, linter, terminal, and markdown preview. Python (i.e. [Anaconda](https://docs.anaconda.com/anaconda/install/windows/)) and [git](https://git-scm.com/download/win) need to be installed too.

In unit 1, we will only use Jupyter notebooks - you do not need an IDE for that. So you do not need to worry about point (4.) for the first week.

# 2. Video: Unit 1, Part 1
Please watch the [video](https://youtu.be/Q_IqJOluGB4).

# 3. Github learning lab
Create a [github account](https://github.com/) and work through the [github learning lab](https://lab.github.com/githubtraining/introduction-to-github). Please send me your github username so that I can add you to our class project page on github.

# 4. Video: Unit 1, Part 2
Please watch the [video](https://youtu.be/Q_IqJOluGB4) (thjs will be a different video).

# 5. Quiz
Answer the [questions](https://forms.gle/NXypPT3QbC33NDiW6) (this is strictly anonymous).

# 6. Live lesson
We will meet on Thursday, March 11th at 12:30 - 3:00 PM for the live lesson. You should have gotten a link via email. You will need a couple of files for the implementation that we will work through in the lesson: [data files](https://github.com/ssciwr/sustainable_development_course/blob/main/downloads/data.zip) and the [main notebook](https://github.com/ssciwr/sustainable_development_course/blob/main/unit1/src/notebook_unit1.ipynb).

During the lesson, we will use [nbstripout](https://github.com/kynan/nbstripout) in conjunction with the [pre-commit package](https://pre-commit.com/).

# 7. Asynchronous work in your team
Continue working on your notebook during the week and complete the remaining tasks. Collaborate through github, and use branches, pull request, and request reviews from your team members before merging any branches into main.

# 8. Evaluation of unit 1
This is not mandatory, but we would highly appreciate your feedback. Please help us by [answering a couple of questions](https://forms.gle/btaafmAo97Zr1Zd3A).
