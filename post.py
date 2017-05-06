try:
    import urllib.request as urlrequest
except ImportError:
    import urllib as urlrequest

import json


def log(type_, data):
    url = 'http://localhost:4020/api/action/' + type_
    urlrequest.urlopen(url, data=json.dumps(data).encode())
    

def get_actions():
    url = 'http://localhost:4020/api/action/?key=bananinha'
    return json.loads(urlrequest.urlopen(url).read())


log("teste", {'albo':[123,1234]})
print(get_actions())
