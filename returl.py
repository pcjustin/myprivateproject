#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
# work on MAC
# brew install python3
# pip3 install re
from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar
import re
import sys

if __name__ == '__main__':
    login_url = 'http://bitly.co'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    head = {'Origin': 'http://bitly.co' , 'Upgrade-Insecure-Requests': '1', 'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    Login_Data = {}
    Login_Data['turl'] = sys.argv[1]
    Login_Data['url_done'] = 'done'  
    logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
    cookie = cookiejar.CookieJar()
    cookie_support = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_support)
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head)
    try:
        response1 = opener.open(req1)
        html = response1.read().decode('utf-8')
        pattern = re.compile('真实网址为：.*?><a href="(.*?)"', re.S)
        items = re.findall(pattern,html)
        for item in items:
            print(item)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError:%d" % e.code)
        elif hasattr(e, 'reason'):
            print("URLError:%s" % e.reason)
