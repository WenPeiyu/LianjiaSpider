

# import modules
import requests
import json


strMD5Salt = "vfkpbin1ix2rb88gfjebs0f60cbvhedl"
dictURL = {
    "search/ershoufang": {
        "URL": "https://ajax.lianjia.com/map/search/ershoufang/?city_id={city_id}&group_type={group_type}&"
               "max_lat={max_lat}&min_lat={min_lat}&max_lng={max_lng}&min_lng={min_lng}&" 
               "filters=%7B%7D&request_ts={request_ts}&source=ljpc&authorization={authorization}",
        "MD5Data": strMD5Salt + "city_id={city_id}group_type={group_type}max_lat={max_lat}"
                                "max_lng={max_lng}min_lat={min_lat}min_lng={min_lng}request_ts={request_ts}"
    },
    "subway/station": {
        "URL": "https://ajax.lianjia.com/map/subway/station/?city_id={city_id}&line_id={line_id}&"
               "request_ts={request_ts}&source=ljpc&authorization={authorization}",
        "MD5Data": strMD5Salt + "city_id={city_id}line_id={line_id}request_ts={request_ts}"
    },
    "subway/line": {
        "URL": "https://ajax.lianjia.com/map/subway/line/?city_id={city_id}&request_ts={request_ts}&source=ljpc"
               "&authorization={authorization}",
        "MD5Data": strMD5Salt + "city_id={city_id}request_ts={request_ts}"
    },
    "resblock/ershoufangcard": {
        "URL": "https://ajax.lianjia.com/map/resblock/ershoufangcard/?id={id}&request_ts={request_ts}&"
               "source=ljpc&authorization={authorization}",
        "MD5Data": strMD5Salt + "id={id}request_ts={request_ts}"
    },
    "resblock/ershoufanglist": {
        "URL": "https://ajax.lianjia.com/map/resblock/ershoufanglist/?id={id}&order={order}&page={page}&"
               "filters=%7B%7D&request_ts={request_ts}&source=ljpc&authorization={authorization}",
        "MD5Data": strMD5Salt + "id={id}order={order}page={page}request_ts={request_ts}"
    },
}

tupleGroupType = (
    "district",     #行政区
    "bizcircle",    #商圈
    "community",    #居民小区
    )

lstCity = [
    ('https://bj.lianjia.com/', '北京'),
    ('https://cd.lianjia.com/', '成都'),
    ('https://cq.lianjia.com/', '重庆'),
    ('https://cs.lianjia.com/', '长沙'),
    ('https://dg.lianjia.com/', '东莞'),
    ('https://dl.lianjia.com/', '大连'),
    ('https://fs.lianjia.com/', '佛山'),
    ('https://gz.lianjia.com/', '广州'),
    ('https://hf.lianjia.com/', '合肥'),
    ('https://hk.lianjia.com/', '海口'),
    ('https://hui.lianjia.com/', '惠州'),
    ('https://hz.lianjia.com/', '杭州'),
    ('https://jn.lianjia.com/', '济南'),
    ('https://lf.lianjia.com/', '廊坊'),
    ('https://nj.lianjia.com/', '南京'),
    ('https://qd.lianjia.com/', '青岛'),
    ('https://sh.lianjia.com/', '上海'),
    ('https://sjz.lianjia.com/', '石家庄'),
    ('https://su.lianjia.com/', '苏州'),
    ('https://sy.lianjia.com/', '沈阳'),
    ('https://sz.lianjia.com/', '深圳'),
    ('https://tj.lianjia.com/', '天津'),
    ('https://wh.lianjia.com/', '武汉'),
    ('https://wx.lianjia.com/', '无锡'),
    ('https://xa.lianjia.com/', '西安'),
    ('https://xm.lianjia.com/', '厦门'),
    ('https://yt.lianjia.com/', '烟台'),
    ('https://zh.lianjia.com/', '珠海'),
    ('https://zs.lianjia.com/', '中山'),
    ('https://zz.lianjia.com/', '郑州')
    ]

dictCity = {
    '长沙': {'city_id': '430100', 'max_lat': '28.368467', 'min_lat': '28.101143', 'max_lng': '113.155889',
           'min_lng': '112.735051'},
    '上海': {'city_id': '310000', 'max_lat': '31.36552', 'min_lat': '31.106158', 'max_lng': '121.600985',
           'min_lng': '121.360095'},
    '北京': {'city_id': '110000', 'max_lat': '40.074766', 'min_lat': '39.609408', 'max_lng': '116.796856',
           'min_lng': '115.980476'},
    '烟台': {'city_id': '370600', 'max_lat': '37.590234', 'min_lat': '37.349651', 'max_lng': '121.698469',
           'min_lng': '121.210365'},
    '厦门': {'city_id': '350200', 'max_lat': '24.794145', 'min_lat': '24.241819', 'max_lng': '118.533083',
           'min_lng': '117.892627'}
    }
