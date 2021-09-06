from importlib.metadata import version
import requests
print(version('requests'))
r = requests.get('http://google.com')
print(r.status_code)