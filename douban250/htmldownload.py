# -*- coding: utf-8 -*-

"""下载器"""

__author__ = 'katherinelove'

import requests

class HtmlDownload(object):
    def download(self,url):
        if url==None or url=="":
            return None
        user_agent="Mozilla/4.0(Compatible;MSIE 5.5; Windows NT)"
        header={"user_agent":user_agent}

        response=requests.get(url,header=header)
        if response.status_code==200:
            response.encoding="utf-8"
            return response.text
        return None
