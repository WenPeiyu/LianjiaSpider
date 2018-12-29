import re
import pandas as pd
import pickle
from log import logger
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class LogFlow:
    """
    日志编码流
    """
    def __init__(self, filepath):
        """
        初始化对象
        :param filepath: 欲处理的日志文件地址
        """
        self.filepath = filepath
        self.logger = logger
        self.read_file()
        self.logger.info("模块{0}初始化成功".format(self.__class__.__name__))

    def read_file(self):
        """
        读入日志文件
        :return:
        """
        self.df_log = pd.read_csv(self.filepath)
        self.logger.info("日志文件 - {file} 载入成功".format(file=self.filepath))
        self.df_log_RA_MSG = self.df_log[self.df_log.MSG + self.df_log.RA > 0]

    def collect_message(self, crnti=None, RA=True):
        """
        提取日志的信息列
        :param crnti: 欲提取的crnti编号，默认为None不具体到具体crnti
        :param RA: 是否开启随机接入过滤，默认开启，否则读取全部日志字段
        :return:
        """
        self.lst_message = []
        if crnti is None:
            if RA:
                self.lst_message = list(self.df_log_RA_MSG["Message"])
            else:
                self.lst_message = list(self.df_log["Message"])
        else:
            if RA:
                df_temp = self.df_log_RA_MSG[self.df_log_RA_MSG.CRNTI == crnti]
                self.lst_message = list(df_temp["Message"])
            else:
                df_temp = self.df_log[self.df_log.CRNTI == crnti]
                self.lst_message = list(df_temp["Message"])

    def extract_information(self):
        """
        提取消息中的字段，格式化为格式数据
        :return:
        """
        self.lst_randomaccess = []
        for i in self.lst_message:
            stra = i
            re_sign = re.compile(r"\[[a-zA-Z]+[a-zA-Z\s0-9]*?\]")
            re_allocate = re.compile(r"[ 0-9a-zA-Z_]+\[[,\:\-a-zA-Z\s0-9]+?\][a-zA-Z]*")
            re_measure = re.compile(r"[0-9a-zA-Z_]+=[-0-9]*")
            sign = re_sign.findall(stra)
            sign = {"sign": [i.strip() for i in sign if i.strip()]}
            stra = re_sign.sub("", stra)
            allocate = re_allocate.findall(stra)
            allocate = [i.strip() for i in allocate if i.strip()]
            allocate = {"allocate": {i.split('[')[0]: i.split('[')[1].replace(']', '') for i in allocate}}
            stra = re_allocate.sub("", stra)
            measure = re_measure.findall(stra)
            measure = [i.strip() for i in measure if i.strip()]
            measure = {"measure": {i.split('=')[0]: i.split('=')[1] for i in measure}}
            stra = re_measure.sub("", stra)
            describe = stra.replace(".", "").split(",")
            describe = {"describe": [
                re.sub("\d+ msg3gid", "msg3gid", re.sub("SFN\[\d+\]", "", re.sub("\| \@\[\d+\]", "", i.strip())))
                for i in describe if i.strip()]}
            self.lst_randomaccess.append({**sign, **allocate, **measure, **describe})

    def generate_tagset(self):
        """
        生成标签集合
        :return:
        """
        sign = []
        allocate = []
        measure = []
        describe = []
        for i in self.lst_randomaccess:
            sign = sign + i['sign']
            sign = list(set(sign))
            measure = measure + list(i["measure"].keys())
            measure = list(set(measure))
            allocate = allocate + list(i["allocate"].keys())
            allocate = list(set(allocate))
            describe = describe + i['describe']
            describe = list(set(describe))
        self.set_tags = (sign, measure, allocate, describe)

    def init_mapping(self):
        """
        生成标签到编码的映射表
        :return:
        """
        tags = []
        attrs = []
        no = []
        sign = self.set_tags[0]
        measure = self.set_tags[1]
        allocate = self.set_tags[2]
        describe = self.set_tags[3]
        tags = tags + list(sign)
        attrs = attrs + len(sign) * ["sign"]
        no1 = [hex(i)[2:].zfill(4) for i in range(len(sign))]
        tags = tags + list(measure)
        attrs = attrs + len(measure) * ["measure"]
        no2 = [hex(i+256)[2:].zfill(4) for i in range(len(measure))]
        tags = tags + list(allocate)
        attrs = attrs + len(allocate) * ["allocate"]
        no3 = [hex(i+1280)[2:].zfill(4) for i in range(len(allocate))]
        tags = tags + list(describe)
        attrs = attrs + len(describe) * ["describe"]
        no4 = [hex(i+2304)[2:].zfill(4) for i in range(len(describe))]
        no = [hex(i)[2:].zfill(4) for i in range(len(sign) + len(measure) + len(allocate) + len(describe))]
        self.df_mapping = pd.DataFrame({
            "tag": tags,
            "attr": attrs,
            "no_order": no,
            "no": no1+no2+no3+no4})

    def dump_mapping(self, path):
        """
        导出映射表
        :param path:
        :return:
        """
        pickle.dump(self.df_mapping, open(path, "wb"))

    def load_mapping(self, path):
        """
        导入映射表
        :param path:
        :return:
        """
        self.df_mapping = pickle.load(open(path, 'rb'))

    def generate_code(self):
        """
        根据映射表将日志消息编码化
        :return:
        """
        for num, i in enumerate(self.lst_randomaccess):
            str_code = ""
            str_code_color = ""
            for j in i:
                for m in i[j]:
                    str_code = str_code + dict(zip(self.df_mapping["tag"], self.df_mapping["no"]))[m]
                    str_code_color = str_code_color + dict(zip(self.df_mapping["tag"], self.df_mapping["no_order"]))[m]
            self.lst_randomaccess[num]["code"] = str_code
            self.lst_randomaccess[num]["code_color"] = str_code_color

    def plot_message_spectrum(self):
        """
        绘制消息流图谱
        :return:
        """
        length = len(self.lst_randomaccess)
        matplotlib.rcParams['figure.figsize'] = [10, length * 0.5]
        plt.figure()
        plt.subplots_adjust(hspace=0)
        for num, i in enumerate(self.lst_randomaccess):
            s = i["code_color"]
            plt.subplot(length, 1, num + 1)
            lst_color = [eval("0x" + s[i:i + 4]) for i in range(0, len(s), 4)]
            arr_color = np.array([lst_color])
            plt.pcolor(arr_color)
            plt.axis('off')

