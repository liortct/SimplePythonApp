import sys
import requests

app = '{{ cookiecutter.app_name }}'

if app.lower() != app:
    print(f"App name must be lower case")
    sys.exit(1)




