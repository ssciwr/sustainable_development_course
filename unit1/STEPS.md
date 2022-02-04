# The required commands in live session 1
## git repos and workflow

See [here](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories).
```
git init
git remote add origin "your-github-repo-url"
git remote -v
git pull origin main
git branch --set-upstream-to=origin/main main
git add "your-file"
git commit -m "your-commit-message"
git push
```
## Using pre-commit hooks
```
pip install pre-commit
pip install --upgrade nbstripout
```
in .pre-commit-config.yml:
```
repos:
  - repo: https://github.com/kynan/nbstripout
    rev: 0.5.0
    hooks:
      - id: nbstripout
        files: ".ipynb"

pre-commit install
```