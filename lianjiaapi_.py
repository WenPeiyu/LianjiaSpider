import json
import time
import hashlib
import requests



def get_line_site(url):
    """请求链接"""
    headers = {'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Host': 'ajax.lianjia.com',
               'Referer': 'https://gz.lianjia.com/ditu/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r


def get_url():
    """拼接链接"""
    b = {"city_id": "310000",
         "group_type": "district",
         "max_lat": "31.404486",
         "min_lat": "31.067068",
         "max_lng": "121.588912",
         "min_lng": "121.372168",
         }
    url ="https://ajax.lianjia.com/map/search/ershoufang/?city_id={city_id}&group_type={group_type}&" \
         "max_lat={max_lat}&min_lat={min_lat}&max_lng={max_lng}&min_lng={min_lng}&" \
         "filters=%7B%7D&request_ts={request_ts}&source=ljpc&" \
         "authorization={authorization}"
    request_ts = int(time.time() * 1000)
    md5_data = "vfkpbin1ix2rb88gfjebs0f60cbvhedlcity_id={city_id}group_type={group_type}max_lat={max_lat}" \
             "max_lng={max_lng}min_lat={min_lat}min_lng={min_lng}request_ts={request_ts}".format(
        city_id=b["city_id"],
        group_type=b["group_type"],
        max_lat=b["max_lat"],
        max_lng=b["max_lng"],
        min_lat=b["min_lat"],
        min_lng=b["min_lng"],
        request_ts=request_ts)
    authorization = get_md5(md5_data)
    url = url.format(request_ts=request_ts, authorization=authorization,city_id=b["city_id"],
        group_type=b["group_type"],
        max_lat=b["max_lat"],
        max_lng=b["max_lng"],
        min_lat=b["min_lat"],
        min_lng=b["min_lng"])
    return url


if __name__ == '__main__':
    line_url = get_url()
    print(line_url)
    res = get_line_site(line_url)
    items = res.json()['data']
    with open('lon_and_lat.txt', 'w') as f:
        json.dump(items, f)

    print(items)

