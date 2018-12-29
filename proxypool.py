import requests
from bs4 import BeautifulSoup
import time


def func():
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "h-CN,zh;q=0.9",
        "connection": "keep-alive",
        "Host": "ip.zdaye.com",
        "Referer": "http://ip.zdaye.com/FreeIPlist.html",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = "http://ip.zdaye.com/FreeIPlist.html"
    res1 = requests.get(url, headers=header)
    res = res1.text.encode(res1.encoding)
    res = BeautifulSoup(res, "lxml")
    return [i.find("td").string for i in res.find("tbody").find_all("tr", class_=False)]


def getvalidlist():
    tag = True
    while tag:
        try:
            a = func()
        except:
            tag = True
        else:
            tag = False
    return a


def verification(proxy_ip, proxy_port):
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "h-CN,zh;q=0.9",
        "connection": "keep-alive",
        "Host": "myip.ipip.net",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    proxy = {
        'http': 'http://%s:%s' % (proxy_ip, proxy_port),
        'https': 'https://%s:%s' % (proxy_ip, proxy_port)
    }
    url = 'http://myip.ipip.net'
    try:
        text = requests.get(url, headers=header, proxies=proxy, timeout=1.5)
        if len(text.text) < 100:
            print(text.text)
            return (proxy_ip, proxy_port)
    except Exception as e:
        print("Error: ", e)




tupleport = ("80", "8080")  # ,"8060","1080","3128","9898")
lst = []
while True:
    a = getvalidlist()
    for proxy_ip in a:
        for proxy_port in tupleport:
            time1 = time.time()
            time2 = time1
            while time2 - time1 < 3:
                m = verification(proxy_ip, proxy_port)
                if type(m) == tuple:
                    with open("e:/wenpeiyu/proxy.txt", "a") as f:
                        f.write("{}\n".format(m))
                        break
                time2 = time.time()
