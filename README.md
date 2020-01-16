# Visual Studio Code Debugger with Django

Reference Django Project Sample: https://docs.djangoproject.com/en/3.0/intro/tutorial01/

## Pre-Install

`pipenv install`


## Use Debugger Local Attach

### Start Local ptvsd server and Web Server

``` bash
pipenv shell
DEBUG=True ./manage.py runserver --noreload
```

### Start Local Attach Debugger

Use VS code Debugger and select Python: Local Attach

Set breakpoint then debug.

## Use Debugger Attach in Docker

### Start Local ptvsd server and Web Server

`docker-compose up`

### Start Attach in Docker Debugger

Use VS code Debugger and select Python: Attach in Docker

Set breakpoint then debug.