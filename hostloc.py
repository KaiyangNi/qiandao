# coding: utf-8

import requests
import os

appid1 = os.getenv('appid1')
appid2 = os.getenv('appid2')
token = os.getenv('token')


def hostloc():
    headers = {'Authorization': token}
    session = requests.Session()
    session.headers.update(headers)
    
    import requests
    import time 
    s = requests.Session()
    s.post("http://www.hostloc.com/member.php", {'username':appid1, 'password':appid2,})
    urls = ["http://www.hostloc.com/space-uid-{}.html".format(str(i)) for i in range(10000, 24000)]
    for i in urls:
      s.get(i)
      time.sleep(3)
    
if __name__ == '__main__':
    hostloc()
