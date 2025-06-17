# The required commands in live session 1

## git repos and workflow

### start locally
```
mkdir my-test-repo
cd my-test-repo
git init -b main
```
Now copy files into your repo, ie. the data files from the course repository:
```
cp -r ~/teaching/sustainable_development_course/data/ .
```
Add the data directory with all files to your repo:
```
git add data
git commit -m "added data files"
```
Now open Github in your browser and click on "Create a new repository": Don't initialize the repo with any files, this will only create conflicts!
Copy the repo url and paste it into the command
```
git remote add origin https://github.com/iulusoy/my-test-repo.git
git push -u origin main
```
Add your username and token. You can generate a token by going to your user account settings, clicking on "Developer Settings" and then "Personal access tokens". This will be your password to login from your local machine, please store it somewhere safe.

### start on the remote and then cloning locally
Create a new repo on GitHub, initialize with a README, .gitignore and License, and clone to your machine using 
```
git clone https://github.com/iulusoy/my-test-repo.git
```
Then you can add files to your repo, add, commit and push them:
```
git add data
git commit -m "added data files"
git push
```

## Creating conda environments
To avoid negative interactions between installed packages and version conflicts, you should create a conda environment for each new project. You do si by executing 
```
conda create --name your-environment-name python=3.11
```
You then activate the environment using 
```
conda activate your-environment-name
```
Install the course requirements via the repo from assignment #2: 
```
pip install -r requirements.txt
```
This will install all necessary Python packages into your conda environment.

## Using pre-commit hooks
```
python -m pip install pre-commit
python -m pip install --upgrade nbstripout
```
in .pre-commit-config.yaml:
```
repos:
  - repo: https://github.com/kynan/nbstripout
    rev: 0.8.1
    hooks:
      - id: nbstripout
        files: ".ipynb"
```
Activate the pre-commit hook using
```
pre-commit install
```