# The required commands in live session 5

# Testing

- use pytest-sugar for nicer styling
- use pytest-cov to determine test coverage of the code

Install Pytest and these packages using
```
python -m pip install pytest
python -m pip install pytest-sugar
python -m pip install pytest-cov
```
You will place your unit tests inside a folder `test` or `tests` inside your `src/` directory. You can then run pytest using 
```
python -m pytest
```
and it will automatically find the tests in your test folder. To get more output, or to enable print output when running pytest, use the `-v`, or `-s` flag.