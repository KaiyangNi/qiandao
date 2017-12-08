# coding: utf-8

import requests
import time
import os
import random

appid1 = os.getenv('appid1')
appid2 = os.getenv('appid2')

def hostloc():
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Referer':'http://www.hostloc.com'}
    session = requests.Session()
    session.headers.update(headers)
    
    s = requests.Session()
    s.post("http://www.hostloc.com/member.php", {'username':appid1, 'password':appid2})
    urls = ["http://www.hostloc.com/space-uid-{}.html".format(str(random.randrange(1, 50000))) for i in range(12)]
    for i in urls:
      s.get(i)
      time.sleep(2)
    
if __name__ == '__main__':
    hostloc()
