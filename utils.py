import time
import os
import json
import hashlib


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
    :return:
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

