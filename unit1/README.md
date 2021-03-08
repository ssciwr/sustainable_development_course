# Unit 1: Introduction to git

In unit 1, you will learn and practice the git basics. Before we start, there are a few items that you will need to work through, to ensure your computer is set up with everything we need for the course.

If you run into problems at any point, please contact us via inga.ulusoy@uni-heidelberg.de or [open an issue on github](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue).

# 0. Prepare for the lesson
## Windows users
### Option A
1. Please install the Ubuntu Subsystem (Windows Subsystem for Linux) following the steps detailed [here](https://www.windowscentral.com/install-windows-subsystem-linux-windows-10) (I would recommend choosing Ubuntu 20.04 LTS).
1. Enable clipboard copy/paste following [this instruction](https://stackoverflow.com/questions/38832230/copy-paste-in-bash-on-ubuntu-on-windows/50050642#50050642).
1. Please install [xming](https://sourceforge.net/projects/xming/) for X11 forwarding.
1. Open a terminal (launch the Ubuntu terminal), you will need to set a username and password.
1. Update/upgrade the pre-installed libraries through  
`sudo apt update`  
`sudo apt upgrade`  
1. Install git  
`sudo apt install git-all`
1. In your terminal, you need to provide your name and email for your first-time git usage:  
```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```
1. Clone the course repository
`git clone https://github.com/ssciwr/sustainable_development_course.git`
1. Change into the course directory, into the preparation folder:  
`cd sustainable_development_course/preparation`
1. Run the install script; this will install necessary libraries etc. for you:  
`source install.sh`  
You will need to type your password/answer with `Y` a couple of times.

### Option B
1. Install [git for Windows](https://git-scm.com/download/win).
1. Install your favorite IDE, for example [Visual Studio Code](https://visualstudio.microsoft.com/downloads/) and make sure that the GitHub extension works.
2. Make sure that python language support/linter is installed.

## Mac users
1. Install Xcode command line tools.

## Linux users
1. Install git  
`sudo apt install git-all`

## All participants  
If you have not yet done so:
1. In your terminal, you need to provide your name and email for your first-time git usage:  
```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```
1. Clone the course repository
`git clone https://github.com/ssciwr/sustainable_development_course.git`
1. Please change into the course directory, preparation folder  
`cd sustainable_development_course/preparation`
1. Run the installation test script by typing
`python test_install.py` or  
`python3 test_install.py` or  
run it in your IDE. Two windows with graphs should pop up, the first one saying "testing matplotlib", the second one "testing seaborn", both of them showing a straight line. The output of the script should approximately read  
```
Testing pandas  
   a  b  c  
0  1  2  3  
1  4  5  6  
The script took 2.1 seconds to run!
```
1. It is recommended to use an IDE (Integrated Development Environment). If you do not have one already, [Visual Studio Code](https://visualstudio.microsoft.com/downloads/) is recommended for Windows; [Atom](https://atom.io/) for Linux users, but should also work on Windows or Mac OS. If you have never used an IDE before, you will need to install a couple of additional packages within the editor, such as python language support, linter, terminal, and markdown preview. Python (i.e. [Anaconda](https://docs.anaconda.com/anaconda/install/windows/)) and [git](https://git-scm.com/download/win) need to be installed too.

In unit 1, we will only use Jupyter notebooks - you do not need an IDE for that. So you do not need to worry about the last point above in the first week.

# 1. Video: Unit 1, Part 1
Please watch the [video](https://youtu.be/TSQjcPAJ9Ds).

# 2. Github learning lab
Create a [github account](https://github.com/) and work through the [github learning lab](https://lab.github.com/githubtraining/introduction-to-github). Please send me your github username so that I can add you to our class project page on github.

# 3. Video: Unit 1, Part 2
Please watch the [video](https://youtu.be/AoDFzRTS8jQ).

# 4. Quiz
Answer the [questions](https://forms.gle/NXypPT3QbC33NDiW6) (this is strictly anonymous).

# 5. Live lesson
We will meet on Thursday, March 11th at 12:30 - 3:00 PM for the live lesson. You should have gotten a link via email.

During the lesson, we will use [nbstripout](https://github.com/kynan/nbstripout) in conjunction with the [pre-commit package](https://pre-commit.com/).

# 6. Asynchronous work in your team
Continue working on your notebook during the week and complete the remaining tasks. Collaborate through github, and use branches, pull request, and request reviews from your team members before merging any branches into main.

# 7. Evaluation of unit 1
This is not mandatory, but we would highly appreciate your feedback. Please help us by [answering a couple of questions](https://forms.gle/btaafmAo97Zr1Zd3A).
