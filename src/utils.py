import time
import os
import json
import hashlib
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

ak = "dASz7ubuSpHidP1oQWKuAK3q"


def get_md5(str_):
    """
    hash function --md5
    :param str_:origin str
    :return:hex digest
    """
    md5 = hashlib.md5()
    md5.update(str_.encode('utf-8'))
    return md5.hexdigest()


def save_file(data, filename, path=os.getcwd(), filetype="txt"):
    """
    save data into files
    :param data:
    :param filename:
    :param path:
    :param filetype:
    """
    if filetype == 'txt':
        with open("{0}/{1}".format(path, filename), "w") as f:
            for i in data:
                f.write("{}\n".format(i))


def get_request_ts():
    """
    get current timestamp for authorization generation
    :return:
    """
    timestamp = int(time.time() * 1000)
    return timestamp


def get_cor(city):
    """
    get the coordinate of the city
    :param city:
    :return:{'lng': 116.39564503787867, 'lat': 39.92998577808024}
    """
    url = "http://api.map.baidu.com/geocoder/v2/?address={city}&output=json&ak={ak}".format(city=city, ak=ak)
    res = requests.get(url).json()["result"]["location"]
    return res


def get_path():
    """

    :return:
    """
    return os.getcwd()


def get_city_list():
    """
    get the full city list at lianjia.com
    :return:
    """
    res = requests.get("https://sh.lianjia.com/city/")
    work = BeautifulSoup(res.text, "lxml")
    res = set([(i["href"], i.string) for i in
               work.find_all("a", href=re.compile(r"(?<=https://)\w+(?=\.lianjia.com/)"), target=False)][:-1])
    citycodemapping = pd.read_csv(r"C:\Users\wenpeiyu\Desktop\citycodemapping.csv")
    dfcitylist = pd.DataFrame({
        "city": [i[1] for i in res],
        "city_url": [i[0] for i in res]})
    dfCityList = pd.merge(dfcitylist, citycodemapping, how="inner", on=["city"])
    lng = [get_cor(i + "市")['lng'] for i in dfCityList.city]
    lat = [get_cor(i + "市")['lat'] for i in dfCityList.city]
    minlng = [i - 0.3 for i in lng]
    minlat = [i - 0.3 for i in lat]
    city = [i for i in dfCityList.city]
    dfCityCor = pd.DataFrame({
        "city": city,
        "max_lat": lat,
        "max_lng": lng,
        "min_lat": minlat,
        "min_lng": minlng
    })
    dfCityList = pd.merge(dfCityList, dfCityCor, how="inner", on=["city"])
    dfCityList = dfCityList.rename(columns={"citycode": "city_id"})
    dfCityList.to_csv(r".\etc\CityList.csv", index=False)



