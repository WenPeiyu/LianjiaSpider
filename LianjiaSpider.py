import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

OriginURL = r"https://sh.lianjia.com/chengjiao/"
RequestHeader ={
"Host": "sh.lianjia.com",
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
"Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9"}


def getBlockList():
