from config import *
from log import logger
from filetrans import UDPClient


Attach = {
    'MsgType': 'Attach',
    'BoxIp': BoxIp,
    'Mode': 1,
    'StartUeId': StartUeId,
    'EndUeId': EndUeId,
    'Interval': 100
}

Detach = {
    'MsgType': 'Detach',
    'BoxIp': BoxIp,
    'StartUeId': StartUeId,
    'EndUeId': EndUeId,
    'Interval': 100
}

UpPing = {
    'MsgType': 'UpPing',
    'BoxIp': BoxIp,
    'PdnIp': pdnIp,
    'StartUeId': StartUeId,
    'EndUeId': EndUeId,
    'Count': 5,
    'Size': 32,
    'Interval': 100,
    'TimeOut': 10000,
    'UeInterval': 100
}

UPackage = {
    'MsgType': 'StartService',
    'BoxIp': BoxIp,
    'StartUeId': StartUeId,
    'EndUeId': EndUeId,
    'Mode': 1,
    'Interval': 0,
    'Period': 10000,
    'DelayTime': 0,
    'Process': 	['U,800,0']
}

DPackage = {
    'MsgType': 'StartService',
    'BoxIp': BoxIp,
    'StartUeId': StartUeId,
    'EndUeId': EndUeId,
    'Mode': 1,
    'Interval': 0,
    'Period': 2000,
    'DelayTime': 0,
    'Process': 	['D,800,0']
    }

ShuiBiao = {
    'MsgType': 'StartService',
    'BoxIp': BoxIp,
    'StartUeId': StartUeId,
    'EndUeId': EndUeId,
    'Mode': 1,
    'Interval': 0,
    'Period': 2000,
    'DelayTime': 0,
    'Process': 	['U,165,0', 'D,24,0']
}

CloseService = {
    'MsgType': 'CloseService'
}

SaveAttach = {
    'MsgType': 'SaveAttach',
    'FileName': 'Attach'
}

SavePing = {
    'MsgType': 'SavePing',
    'FileName': 'Ping'
}

SaveUeState = {
    'MsgType': 'SaveUeState',
    'FileName': 'UeState'
}

SaveAttachDelay = {
    'MsgType': 'SaveAttachDelay',
    'FileName': 'AttachDelay'
}

SaveMeasure = {
    'MsgType': 'SaveMeasure',
    'FileName': 'Measure'
}

ClearAttach = {
    'MsgType': 'ClearAttach'
}

ClearPing = {
    'MsgType': 'ClearPing'
}

ClearUeState = {
    'MsgType': 'ClearUeState'
}

ClearAttachDelay = {
    'MsgType': 'ClearAttachDelay'
}

ClearSignal = {
    'MsgType': 'ClearSignal'
}


class MK500:
    def __init__(self, dstip=None, dstport=None, boxip=None, pdnip=None,
                 startueid=None, endueid=None):
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
        if startueid is None:
            self.StartUeId = StartUeId
        else:
            self.StartUeId = startueid
        if endueid is None:
            self.EndUeId = EndUeId
        else:
            self.EndUeId = endueid
        self.Command = {
            "Attach": Attach,
            "Detach": Detach,
            "UpPing": UpPing,
            "UPackage": UPackage,
            "DPackage": DPackage,
            "ShuiBiao": ShuiBiao,
            "CloseService": CloseService,
            "Save": [SaveAttach, SavePing, SaveUeState, SaveAttachDelay, SaveAttachDelay],
            "Clear": [ClearAttach, ClearAttachDelay, ClearPing, ClearSignal, ClearUeState]
        }
        self.client = UDPClient(self.dstIP, self.dstPort)
        self.logger.info("{0}初始化成功".format(__class__.__name__))

    def attach(self):
        self.client.sendmsg(self.Command["Attach"])
        self.logger.info("发送Attach命令到{0}".format(self.dstIP))

    def detach(self):
        self.client.sendmsg(self.Command["Detach"])
        self.logger.info("发送Detach命令到{0}".format(self.dstIP))

    def save(self):
        self.client.sendmsg(self.Command["Save"])
        self.logger.info("发送保存窗口记录命令到{0}".format(self.dstIP))

    def clear(self):
        self.client.sendmsg(self.Command["Clear"])
        self.logger.info("发送清空窗口命令到{0}".format(self.dstIP))

    def close(self):
        self.client.sendmsg(self.Command["CloseService"])
        self.logger.info("发送关闭服务命令到{0}".format(self.dstIP))

    def ping(self):
        self.client.sendmsg(self.Command["UpPing"])
        self.logger.info("发送Ping {1}命令到{0}".format(self.dstIP, self.pdnIp))

    def upload(self):
        self.client.sendmsg(self.Command["UPackage"])
        self.logger.info("发送上行灌包命令到{0}".format(self.dstIP))

    def download(self):
        self.client.sendmsg(self.Command["DPackage"])
        self.logger.info("发送下行灌包命令到{0}".format(self.dstIP))

a = MK500()
a.attach()