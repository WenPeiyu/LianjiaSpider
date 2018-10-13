from ftplib import FTP, error_perm
from utils import *
from log import logger
import socket


class FTPClient(object):

    """
    包含上传下载功能的FTP客户端
    例子1(从3GPP协议存储网站下载38系列全部协议):
    >>>client = FTPClient("ftp.3gpp.org", 21, "anonymous")
    >>>client.connect()
    >>>a.download(r"/Specs/archive/38_series/", "H:/specs", "nlst") # 不支持mlsd检索目录的网站可用nlst方法替代
    例子2(开通ftp服务器的本地的上传下载演示):
    >>>client = FTPClient("127.0.0.1", 21, "root", "root")
    >>>client.connect()
    >>>client.upload("/test/", "h:/folder1/")
    >>>client.download("/test/", "h:/folder2/")
    """
    def __init__(self, host, port=21, username=None, password=None):
        """
        初始化
        :param host: 主机
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        self.logger = logger

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = FTP()
        self.logger.info("{0}初始化成功".format(self.__class__.__name__))

    def connect(self):
        """
        连接并登录FTP服务器
        """
        try:
            res = self.client.connect(self.host, self.port)
            self.logger.info("连接{0}成功".format(self.host))
            self.logger.debug(res)
            try:
                res = self.client.login(self.username, self.password)
                self.logger.info("账户{0}登录成功".format(self.username))
                self.logger.debug(res)
            except Exception as e:
                self.logger.error("账户{0}登录失败".format(self.username))
                self.logger.debug(e)
        except Exception as e:
            self.logger.error("连接{0}失败".format(self.host))
            self.logger.debug(e)

    def _download_file(self, remote_path, local_path):
        """
        从远程路径下载单文件文件到本地路径
        :param remote_path: 远程路径
        :param local_path: 本地路径
        """
        try:
            handle = open(local_path, "wb")
            res = self.client.retrbinary("RETR %s" % remote_path, handle.write, 1024)
            handle.close()
            self.logger.info("文件{0}下载成功".format(remote_path))
            self.logger.debug(res)
        except Exception as e:
            self.logger.error("文件{0}下载失败".format(remote_path))
            self.logger.debug(e)

    def _download_nlst(self, remote_path, local_path):
        """
        nlst方式检索的下载方法
        :param remote_path: 远程路径
        :param local_path: 本地路径
        :return:
        """
        # 判断远程路径是文件还是文件夹
        try:
            self.client.cwd(remote_path)
        except:
            current_remote_type = "file"
        else:
            current_remote_type = "dir"

        # 文件直接调用下载之
        if current_remote_type == "file":
            current_local_path = local_path + "/" + os.path.basename(remote_path)
            self._download_file(remote_path, current_local_path)
        # 文件夹进入文件夹递归调用本function
        elif current_remote_type == "dir":
            current_local_path = local_path + "/" + os.path.basename(remote_path)
            try:
                os.makedirs(current_local_path)
                self.logger.info("文件夹{0}创建成功".format(current_local_path))
            except FileExistsError:
                self.logger.debug("文件夹{0}已经存在".format(current_local_path))
            for i in self.client.nlst(remote_path):
                self._download_nlst(i, current_local_path)

    def download(self, remote_path, local_path, method="mlsd"):
        """
        将远程目录下所有内容下载到本地目录下
        :param remote_path: 远程路径
        :param local_path: 本地路径
        :param method: FTP服务器目录遍历方式(mlsd或者nlst)
        """
        # 验证远程目录是否包含中文
        if contain_zh(remote_path):
            self.logger.error("远程路径包含中文")
            return -1

        # 验证本地路径是否存在
        try:
            os.chdir(local_path)
        except FileNotFoundError:
            os.mkdir(local_path)
            self.logger.info("文件夹{0}创建成功".format(local_path))

        # 遍历远程路径文件与文件夹
        if method == "nlst":
            self._download_nlst(remote_path, local_path)
            return 1
        for i in self.client.mlsd(remote_path):
            current_remote_type = i[1]["type"]
            # 若是文件则调用直接download_file下载之
            if current_remote_type == "file":
                current_remote_path = remote_path + i[0]
                current_local_path = local_path + i[0]
                self._download_file(current_remote_path, current_local_path)
            # 若是文件夹则递归调用本function
            elif current_remote_type == "dir":
                current_remote_path = remote_path + i[0] + "/"
                current_local_path = local_path + i[0] + "/"
                try:
                    os.makedirs(current_local_path)
                    self.logger.info("文件夹{0}创建成功".format(current_local_path))
                except FileExistsError:
                    self.logger.debug("文件夹{0}已经存在".format(current_local_path))
                self.download(current_remote_path, current_local_path)

    def _upload_file(self, remote_path, local_path):
        """
        从本地路径上传单文件到远程路径
        :param remote_path: 远程路径
        :param local_path: 本地路径
        """
        try:
            handle = open(local_path, "rb")
            res = self.client.storbinary("STOR %s" % remote_path, handle, 1024)
            handle.close()
            self.logger.info("文件{0}上传成功".format(remote_path))
            self.logger.debug(res)
        except Exception as e:
            self.logger.error("文件{0}上传失败".format(remote_path))
            self.logger.debug(e)

    def upload(self, remote_path, local_path):
        """
        上传本地路径内容到远程路径
        :param remote_path:
        :param local_path:
        :return:
        """
        # 验证远程目录是否包含中文
        if contain_zh(remote_path):
            self.logger.error("远程路径包含中文")
            return -1

        # 遍历本地路径文件及文件夹
        if os.path.exists(local_path):
            # 若是文件则直接调用upload_file上传之
            if os.path.isfile(local_path):
                self._upload_file(remote_path, local_path)
            # 若是文件夹则dir展开文件夹递归调用本function
            elif os.path.isdir(local_path):
                # 验证远程目录是否存在
                try:
                    self.client.cwd(remote_path)
                    self.logger.info("文件夹{0}已存在".format(remote_path))
                except error_perm:
                    try:
                        self.client.mkd(remote_path)
                        self.logger.info("文件夹{0}创建成功".format(remote_path))
                    except error_perm:
                        self.logger.error("无创建文件夹权限")
                        return -1
                local_path = local_path + "/"
                remote_path = remote_path + "/"
                for i in os.listdir(local_path):
                    current_remote_path = remote_path + i
                    current_local_path = local_path + i
                    self.upload(current_remote_path, current_local_path)


class UDPClient(object):
    def __init__(self, host, port):
        self.logger = logger
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = None
        self.logger.info("{0}初始化成功".format(__class__.__name__))

    def sendmsg(self, msg):
        """
        发送消息
        :param msg:
        :return:
        """
        msg = str(msg)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.sendto(str(msg).encode(), self.address)
        self.logger.debug("发送消息{0}到{1}".format(msg, self.address))
        self.socket.close()


class TCPClient(object):
    def __init__(self, host, port):
        self.logger = logger
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.info("{0}初始化成功".format(__class__.__name__))






# a = FTPClient("ftp.3gpp.org", 21, "anonymous")
# a.connect()
# a.download(r"/Specs/archive/38_series/", "H:/3GPPSpecs", "nlst")


# client = FTPClient("10.63.153.212", 21, "root", "root")
# client.connect()
# client.download("/9.13VolumeTest/", "h:/downloadtest/")

