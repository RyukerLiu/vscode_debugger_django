#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_project.settings')
    try:
        from django.core.management import execute_from_command_line

        # add ptvsd for vscode debugger
        DEBUG = os.environ.get('DEBUG')
        if DEBUG:
            # Check isMainProcess to avoid create two ptvsd server in same address error when hot reload
            isMainProcess = os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN')
            if isMainProcess:
                import ptvsd
                address = ('0.0.0.0', 5678)
                ptvsd.enable_attach(address=address)
                print('!!! In Debug Mode !!!')
                print('Create ptvsd server at', address)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
