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
1. Run the install script; this will install necessary libraries etc. for you:  
`source install.sh`  
You will need to type your password/answer with Y a couple of times.

1. Run the installation test script by typing
`python test_install.py` or  
`python3 test_install.py` or  
run it in your IDE. Two windows with graphs should pop up, the first one saying "testing matplotlib", the second one "testing seaborn", both of them showing a straight line, and you need to close the windows using the "x". The output of the script should approximately read  
```
Testing pandas  
   a  b  c  
0  1  2  3  
1  4  5  6  
The script took 2.1 seconds to run!
```