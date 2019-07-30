"""
Created by 零柒叁 on 2019/7/30
"""

from urllib import  request
import requests

class HTTP:
    def get(self,url,return_json=True):
        r = requests.get(url)
        return r
        pass