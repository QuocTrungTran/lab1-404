from importlib.metadata import version
import requests
print(version('requests'))
r = requests.get('http://google.com')
print(r.status_code)


r1 =  requests.get('https://raw.githubusercontent.com/QuocTrungTran/lab1-404/master/Lab1.py?flush_cache=true')
print(r1.text)

