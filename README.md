# Visual Studio Code Debugger with Django

Reference Django Project Sample: https://docs.djangoproject.com/en/3.0/intro/tutorial01/

## Pre-Install

`pipenv install`


## Use Local Attach

### Start Local ptvsd server

``` bash
pipenv shell
DEBUG=True ./manage.py runserver --noreload
```

### Start Local Attach Debugger

Use VS code Debugger and select Python: Local Attach

Set breakpoint then debug.

