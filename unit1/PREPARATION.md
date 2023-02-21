# 0. Prepare for the lesson
## Windows users
1. Install [git for Windows](https://git-scm.com/download/win).
1. Install [Anaconda for Windows](https://www.anaconda.com/).
1. Optional: Install your favorite IDE, for example [Visual Studio Code](https://visualstudio.microsoft.com/downloads/) Community Edition and make sure that the GitHub extension works.
1. For VSCode: Make sure that python language support/linter is installed ([see here](https://code.visualstudio.com/docs/python/python-tutorial)).

## Mac users
1. Install Xcode command line tools.

## Linux users
1. Install git  
`sudo apt install git-all`

## All participants  
If you have not yet done so:
1. In your terminal (if on Windows: choose "Anaconda Powershell Prompt"), you need to provide your name and email for your first-time git usage:  
```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```
1. Clone the course repository (in your terminal)  
`git clone https://github.com/ssciwr/sustainable_development_course.git`
1. Please change into the course directory  
`cd sustainable_development_course`
1. Create a new conda environment  
`conda create --name ssd-course python==3.9`
1. Activate your new conda environment  
`conda activate ssd-course`
1. Install the required Python libraries:  
`pip install -r requirements.txt`
1. Run the installation test script by changing into the "preparation" folder and running the Python script:
```
cd preparation
python test_install.py
```  
Or run it in your IDE. Two windows with graphs should pop up, the first one saying "testing matplotlib", the second one "testing seaborn", both of them showing a straight line, and you need to close the windows using the "x". The output of the script should approximately read  
```
Testing pandas  
   a  b  c  
0  1  2  3  
1  4  5  6  
The script took 2.1 seconds to run!
```
1. Test if Jupyter is running: In your anaconda prompt, type `jupyter-notebook`. If a window pops up asking you with which App to open the Notebook, choose your favorite browser.
1. If on Windows, you can also open Jupyter from the Anaconda Navigator, just make sure to select the correct conda environment before launching Jupyter.
