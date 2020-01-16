# Visual Studio Code Debugger with Django

Reference Django Project Sample: https://docs.djangoproject.com/en/3.0/intro/tutorial01/

Reference: https://gist.github.com/veuncent/1e7fcfe891883dfc52516443a008cfcb

Reference for hot reload with debugger: https://ytec.nl/blog/debugging-django-vscode-without-using-noreload/


## Use Debugger Local Attach

### Pre-Install

`pipenv install`

### Start Local ptvsd server and Web Server

``` bash
pipenv shell
DEBUG=True ./manage.py runserver
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