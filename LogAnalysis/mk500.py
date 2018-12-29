from config import *
from log import logger
from filetrans import UDPClient
from utils import *


class MK500:
    def __init__(self, dstip=None, dstport=None, boxip=None, pdnip=None):
        self.logger = logger
        if dstip is None:
            self.dstIP = dstIP
        else:
            self.dstIP = dstip
        if dstport is None:
            self.dstPort = dstPort
        else:
            self.dstPort = dstport
        if boxip is None:
            self.BoxIp = BoxIp
        else:
            self.BoxIp = boxip
        if pdnip is None:
            self.pdnIp = pdnIp
        else:
            self.pdnIp = pdnip

        self.CloseService = {
            'MsgType': 'CloseService'
        }

        self.SaveAttach = {
            'MsgType': 'SaveAttach',
            'FileName': 'Attach'
        }

        self.SavePing = {
            'MsgType': 'SavePing',
            'FileName': 'Ping'
        }

        self.SaveUeState = {
            'MsgType': 'SaveUeState',
            'FileName': 'UeState'
        }

        self.SaveAttachDelay = {
            'MsgType': 'SaveAttachDelay',
            'FileName': 'AttachDelay'
        }

        self.SaveMeasure = {
            'MsgType': 'SaveMeasure',
            'FileName': 'Measure'
        }

        self.ClearAttach = {
            'MsgType': 'ClearAttach'
        }

        self.ClearPing = {
            'MsgType': 'ClearPing'
        }

        self.ClearUeState = {
            'MsgType': 'ClearUeState'
        }

        self.ClearAttachDelay = {
            'MsgType': 'ClearAttachDelay'
        }

        self.ClearSignal = {
            'MsgType': 'ClearSignal'
        }

        self.Command = {
            "CloseService": self.CloseService,
            "Save": [self.SaveAttach, self.SavePing, self.SaveUeState, self.SaveAttachDelay, self.SaveMeasure],
            "Clear": [self.ClearAttach, self.ClearAttachDelay, self.ClearPing, self.ClearSignal, self.ClearUeState]
        }
        self.client = UDPClient(self.dstIP, self.dstPort)
        self.logger.info("{0}初始化成功".format(__class__.__name__))

    def attach(self, start, end):
        attach = {
            'MsgType': 'Attach',
            'BoxIp': self.BoxIp,
            'Mode': 1,
            'StartUeId': start,
            'EndUeId': end,
            'Interval': 100
        }
        self.client.sendmsg(attach)
        self.logger.info("发送Attach命令到{0}".format(self.dstIP))

    def detach(self, start, end):
        detach = {
            'MsgType': 'Detach',
            'BoxIp': self.BoxIp,
            'StartUeId': start,
            'EndUeId': end,
            'Interval': 100
        }
        self.client.sendmsg(detach)
        self.logger.info("发送Detach命令到{0}".format(self.dstIP))

    def save(self):
        for i in self.Command["Save"]:
            self.client.sendmsg(i)
        self.logger.info("发送保存窗口记录命令到{0}".format(self.dstIP))

    def clear(self):
        for i in self.Command["Clear"]:
            self.client.sendmsg(i)
        self.logger.info("发送清空窗口命令到{0}".format(self.dstIP))

    def close(self):
        self.client.sendmsg(self.Command["CloseService"])
        self.logger.info("发送关闭服务命令到{0}".format(self.dstIP))

    def ping(self, start, end):
        ping = {
            'MsgType': 'UpPing',
            'BoxIp': self.BoxIp,
            'PdnIp': self.pdnIp,
            'StartUeId': start,
            'EndUeId': end,
            'Count': 360000,
            'Size': 32,
            'Interval': 100,
            'TimeOut': 10000,
            'UeInterval': 100
        }
        self.client.sendmsg(ping)
        self.logger.info("发送Ping {1}命令到{0}".format(self.dstIP, self.pdnIp))

    def upload(self, start, end):
        upackage = {
            'MsgType': 'StartService',
            'BoxIp': self.BoxIp,
            'StartUeId': start,
            'EndUeId': end,
            'Mode': 1,
            'Interval': 0,
            'Period': 20000,
            'DelayTime': 0,
            'Process': ['U,800,0']
        }
        self.client.sendmsg(upackage)
        self.logger.info("发送上行灌包命令到{0}".format(self.dstIP))
    def download(self, start, end):
        dpackage = {
            'MsgType': 'StartService',
            'BoxIp': self.BoxIp,
            'StartUeId': start,
            'EndUeId': end,
            'Mode': 1,
            'Interval': 0,
            'Period': 20000,
            'DelayTime': 0,
            'Process': ['D,800,0']
        }
        self.client.sendmsg(dpackage)
        self.logger.info("发送下行灌包命令到{0}".format(self.dstIP))

    def shuibiao(self, start, end):
        shuibiao = {
            'MsgType': 'StartService',
            'BoxIp': self.BoxIp,
            'StartUeId': start,
            'EndUeId': end,
            'Mode': 1,
            'Interval': 0,
            'Period': 20000,
            'DelayTime': 0,
            'Process': ['U,165,0', 'D,24,0']
        }

        self.client.sendmsg(shuibiao)
        self.logger.info("发送模拟水表读数上报命令到{0}".format(self.dstIP))

    def danche(self, start, end):
        danche = {
            'MsgType': 'StartService',
            'BoxIp': self.BoxIp,
            'StartUeId': start,
            'EndUeId': end,
            'Mode': 1,
            'Interval': 0,
            'Period': 20000,
            'DelayTime': 0,
            'Process': ['D,160,0', 'U,86,0', 'D,27,0']
        }
        self.client.sendmsg(danche)
        self.logger.info("发送模拟单车开锁命令到{0}".format(self.dstIP))

    def pos(self, start, end):
        pos = {
            'MsgType': 'StartService',
            'BoxIp': self.BoxIp,
            'StartUeId': start,
            'EndUeId': end,
            'Mode': 1,
            'Interval': 0,
            'Period': 20000,
            'DelayTime': 0,
            'Process': ['U,181,0', 'D,218,0']
        }
        self.client.sendmsg(pos)
        self.logger.info("发送模拟Pos机命令到{0}".format(self.dstIP))
