from importlib.metadata import version
import requests
print('Version of requests: ' + version('requests')) #display version of requests library

r = requests.get('http://google.com')
print(r.status_code)

print('-----------------------------------')
r1 =  requests.get('https://raw.githubusercontent.com/QuocTrungTran/lab1-404/master/Lab1.py?flush_cache=true')
print(r1.text)

