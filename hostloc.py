# coding: utf-8

import requests
import time
import os
import random

appid1 = os.getenv('appid1')
appid2 = os.getenv('appid2')
appid3 = os.getenv('appid3')
appid4 = os.getenv('appid4')

def hostloc():
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Referer':'http://www.hostloc.com'}
    s = requests.Session()
    s.headers.update(headers)
    s.post("https://www.hostloc.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lp2tl&inajax=1", {'username':appid1, 'password':appid2})
    urls = ["https://www.hostloc.com/space-uid-{}.html".format(str(random.randrange(10000, 25000))) for i in range(12)]
    for i in urls:
      s.get(i)
      print(i)
        
    s2 = requests.Session()
    s2.headers.update(headers)
    s2.post("https://www.hostloc.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lp2tl&inajax=1", {'username':appid3, 'password':appid4})
    urls = ["https://www.hostloc.com/space-uid-{}.html".format(str(random.randrange(10000, 25000))) for i in range(12)]
    for i in urls:
      s2.get(i)
      print(i)
    
if __name__ == '__main__':
    hostloc()
