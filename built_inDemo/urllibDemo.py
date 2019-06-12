# -*- coding: utf-8 -*-

"""urllib application"""

__author__ = 'katherinelove'


from urllib import request
import requests

if __name__ == '__main__':
    print("===================urllib========================")
    with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
        data=f.read()
        print("status:",f.status,f.reason)
        for k,v in f.getheaders():
            print("%s:%s"%(k,v))
        print("data:",data.decode("utf-8"))
    print("===================requests========================")
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
    response=requests.get("https://api.douban.com/v2/book/2129650",headers=header,verify=False)
    print("history:",response.history)
    print("url:",response.url)
    # print("headers:",response.headers)
    print(response.text)
    print("===================requests豆瓣========================")
    user_agent="'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) " \
               "Version/8.0 Mobile/10A5376e Safari/8536.25"
    headers={"user_agent":user_agent}
    data=requests.get("http://www.douban.com/",headers=headers)
    print("history:", data.history)
    print("url:", data.url)
    print("headers:", data.headers)
    print("iphone 移动版:",data.text)