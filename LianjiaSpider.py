import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

OriginURL = r"https://sh.lianjia.com/chengjiao/"
Header ={
"Host": "sh.lianjia.com",
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
"Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9"}


def get_block_list(url):
    _connection = requests.get(url, header=Header)
    _BS = BeautifulSoup(_connection.text, "lxml")
    _BlockListOrigin = _BS.find("div", class_="position").find_all("a", href=re.compile("/chengjiao/\w+/"), rel=False)
    _BlockList = ["https://sh.lianjia.com" + i["href"] for i in _BlockListOrigin]
    return _BlockList


def get_block_list_of_a_city(url):
    _BlockList = []
    _connection = requests.get(url, header=Header)
    _BS = BeautifulSoup(_connection.text, "lxml")
    _DistrictListOrigin = _BS.find_all("a", href=re.compile("/chengjiao/\w+/"), title=re.compile("上海"))
    _DistrictList = ["https://sh.lianjia.com" + i["href"] for i in _DistrictListOrigin]
    print("Fetched the {}".format(url))
    for i in _DistrictList:
        templist = get_block_list(i)
        _BlockList = _BlockList + templist
        print("Fetched the {}".format(i))
    _BlockList = set(_BlockList)-set(_DistrictList)
    return _BlockList
