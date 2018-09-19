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

dictCity = {
    '珠海': {'city_url': 'https://zh.lianjia.com/',
           'city_id': 440400,
           'max_lat': 22.256915,
           'max_lng': 113.562447,
           'min_lat': 21.956915,
           'min_lng': 113.262447},
    '长沙': {'city_url': 'https://cs.lianjia.com/',
           'city_id': 430100,
           'max_lat': 28.213478,
           'max_lng': 112.979353,
           'min_lat': 27.913478,
           'min_lng': 112.679353},
    '深圳': {'city_url': 'https://sz.lianjia.com/',
           'city_id': 440300,
           'max_lat': 22.546054,
           'max_lng': 114.025974,
           'min_lat': 22.246054,
           'min_lng': 113.725974},
    '重庆': {'city_url': 'https://cq.lianjia.com/',
           'city_id': 500000,
           'max_lat': 29.544606,
           'max_lng': 106.530635,
           'min_lat': 29.244606,
           'min_lng': 106.230635},
    '苏州': {'city_url': 'https://su.lianjia.com/',
           'city_id': 320500,
           'max_lat': 31.317987,
           'max_lng': 120.619907,
           'min_lat': 31.017987,
           'min_lng': 120.319907},
    '西安': {'city_url': 'https://xa.lianjia.com/',
           'city_id': 610100,
           'max_lat': 34.2778,
           'max_lng': 108.953098,
           'min_lat': 33.9778,
           'min_lng': 108.653098},
    '廊坊': {'city_url': 'https://lf.lianjia.com/',
           'city_id': 131000,
           'max_lat': 39.518611,
           'max_lng': 116.703602,
           'min_lat': 39.218611,
           'min_lng': 116.403602},
    '北京': {'city_url': 'https://bj.lianjia.com/',
           'city_id': 110000,
           'max_lat': 39.929986,
           'max_lng': 116.395645,
           'min_lat': 39.629986,
           'min_lng': 116.095645},
    '济南': {'city_url': 'https://jn.lianjia.com/',
           'city_id': 370100,
           'max_lat': 36.682785,
           'max_lng': 117.024967,
           'min_lat': 36.382785,
           'min_lng': 116.724967},
    '郑州': {'city_url': 'https://zz.lianjia.com/',
           'city_id': 410100,
           'max_lat': 34.75661,
           'max_lng': 113.649644,
           'min_lat': 34.45661,
           'min_lng': 113.349644},
    '天津': {'city_url': 'https://tj.lianjia.com/',
           'city_id': 120000,
           'max_lat': 39.14393,
           'max_lng': 117.210813,
           'min_lat': 38.84393,
           'min_lng': 116.910813},
    '厦门': {'city_url': 'https://xm.lianjia.com/',
           'city_id': 350200,
           'max_lat': 24.489231,
           'max_lng': 118.103886,
           'min_lat': 24.189231,
           'min_lng': 117.803886},
    '成都': {'city_url': 'https://cd.lianjia.com/',
           'city_id': 510100,
           'max_lat': 30.679943,
           'max_lng': 104.067923,
           'min_lat': 30.379943,
           'min_lng': 103.767923},
    '沈阳': {'city_url': 'https://sy.lianjia.com/',
           'city_id': 210100,
           'max_lat': 41.808645,
           'max_lng': 123.432791,
           'min_lat': 41.508645,
           'min_lng': 123.132791},
    '大连': {'city_url': 'https://dl.lianjia.com/',
           'city_id': 210200,
           'max_lat': 38.94871,
           'max_lng': 121.593478,
           'min_lat': 38.64871,
           'min_lng': 121.293478},
    '上海': {'city_url': 'https://sh.lianjia.com/',
           'city_id': 310000,
           'max_lat': 31.249162,
           'max_lng': 121.487899,
           'min_lat': 30.949162,
           'min_lng': 121.187899},
    '石家庄': {'city_url': 'https://sjz.lianjia.com/',
            'city_id': 130100,
            'max_lat': 38.048958,
            'max_lng': 114.522082,
            'min_lat': 37.748958,
            'min_lng': 114.222082},
    '南京': {'city_url': 'https://nj.lianjia.com/',
           'city_id': 320100,
           'max_lat': 32.057236,
           'max_lng': 118.778074,
           'min_lat': 31.757236,
           'min_lng': 118.478074},
    '青岛': {'city_url': 'https://qd.lianjia.com/',
           'city_id': 370200,
           'max_lat': 36.105215,
           'max_lng': 120.384428,
           'min_lat': 35.805215,
           'min_lng': 120.084428},
    '广州': {'city_url': 'https://gz.lianjia.com/',
           'city_id': 440100,
           'max_lat': 23.120049,
           'max_lng': 113.30765,
           'min_lat': 22.820049,
           'min_lng': 113.00765},
    '佛山': {'city_url': 'https://fs.lianjia.com/',
           'city_id': 440600,
           'max_lat': 23.035095,
           'max_lng': 113.134026,
           'min_lat': 22.735095,
           'min_lng': 112.834026},
    '武汉': {'city_url': 'https://wh.lianjia.com/',
           'city_id': 420100,
           'max_lat': 30.581084,
           'max_lng': 114.3162,
           'min_lat': 30.281084,
           'min_lng': 114.0162},
    '海口': {'city_url': 'https://hk.lianjia.com/',
           'city_id': 460100,
           'max_lat': 20.022071,
           'max_lng': 110.330802,
           'min_lat': 19.722071,
           'min_lng': 110.030802},
    '烟台': {'city_url': 'https://yt.lianjia.com/',
           'city_id': 370600,
           'max_lat': 37.536562,
           'max_lng': 121.309555,
           'min_lat': 37.236562,
           'min_lng': 121.009555},
    '中山': {'city_url': 'https://zs.lianjia.com/',
           'city_id': 442000,
           'max_lat': 22.545178,
           'max_lng': 113.42206,
           'min_lat': 22.245178,
           'min_lng': 113.12206},
    '无锡': {'city_url': 'https://wx.lianjia.com/',
           'city_id': 320200,
           'max_lat': 31.570037,
           'max_lng': 120.305456,
           'min_lat': 31.270037,
           'min_lng': 120.005456},
    '惠州': {'city_url': 'https://hui.lianjia.com/',
           'city_id': 441300,
           'max_lat': 23.11354,
           'max_lng': 114.410658,
           'min_lat': 22.81354,
           'min_lng': 114.110658},
    '东莞': {'city_url': 'https://dg.lianjia.com/',
           'city_id': 441900,
           'max_lat': 23.043024,
           'max_lng': 113.763434,
           'min_lat': 22.743024,
           'min_lng': 113.463434},
    '杭州': {'city_url': 'https://hz.lianjia.com/',
           'city_id': 330100,
           'max_lat': 30.259244,
           'max_lng': 120.219375,
           'min_lat': 29.959244,
           'min_lng': 119.919375},
    '合肥': {'city_url': 'https://hf.lianjia.com/',
           'city_id': 340100,
           'max_lat': 31.866942,
           'max_lng': 117.282699,
           'min_lat': 31.566942,
           'min_lng': 116.982699}}

dictGroupType = {
    "district": 0.3,  # 行政区
    "bizcircle": 0.08,  # 商圈
    "community": 0.01  # 居民小区
}
