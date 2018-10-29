import re
import os
import time
import sys


def contain_zh(word):
    """
    判断传入字符串是否包含中文
    :param word: 待判断字符串
    :return: True:包含中文  False:不包含中文
    """
    zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zh_pattern.search(word)
    if match:
        return True
    else:
        return False


def dir_list(path, filter_=None, dir_=False):
    """
    获得路径的所有文件列表
    :param path: 目标路径
    :param filter_: 过滤器（正则表达式） 默认不开启
    :param dir_: 文件夹开关 True:返回结果包含文件夹 False:返回结果不含文件夹
    :return: list
    """
    file_list = []
    # 判断文件夹是否可读
    try:
        os.chdir(path)
    except PermissionError:
        return None
    # 展开文件夹做循环
    for i in os.listdir(path):
        # 利用正则表达式做筛选
        if filter_ is None:
            boolean_filter = True
        else:
            ignore_pattern = re.compile(filter_)
            if ignore_pattern.match(i):
                boolean_filter = True
            else:
                boolean_filter = False
        current_path = os.path.join(path, i)
        # 若当前文件项是文件则放入输出列表中
        if os.path.isfile(current_path):
            if not boolean_filter:
                continue
            file_list.append(current_path)
        # 若当前文件项是文件夹则递归循环本函数
        elif os.path.isdir(current_path):
            try:
                if dir_:
                    file_list.append(current_path)
                file_list = file_list + dir_list(current_path, filter_, dir_)
            except TypeError:
                pass
    return file_list


def time_ymd():
    """
    获取当前年月日
    :return: 当前年月日 例:"20181012"
    """
    return time.strftime("%Y%m%d", time.localtime(time.time()))


def time_sleep(sec):
    time.sleep(sec)


def time_ymdhm():
    """
    获取当前年月日
    :return: 当前年月日 例:"20181012"
    """
    return time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
