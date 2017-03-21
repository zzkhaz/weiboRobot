# -*- coding: utf-8 -*-
#from weibopy.api import API
from weibo import Client
import os

API_KEY = '2288083079' #你申请的APP_KEY
API_SECRET = 'adda570146e57c54511153ef7b5167e3' #你申请的APP_SECRET 
REDIRECT_URI = 'https://api.weibo.com/oauth2/default.html' #回调地址
USERID = '250523927@qq.com' #微博账号
PASSWD = 'h1a2z3_87251189' #微博密码

def send():
    c = Client(API_KEY, API_SECRET, REDIRECT_URI, username=USERID, password=PASSWD)
    f = open('test.jpg', 'rb')
    c.post('statuses/upload', status='new weibo!', pic=f)    
    f.close()

send()
