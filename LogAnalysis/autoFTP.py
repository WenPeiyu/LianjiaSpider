from filetrans import FTPClient
from config import *
from utils import *
from log import logger
from multiprocessing import Pool


def run_ftp(ftp_para, ftp_paras, interval=60, continuous=False, size_=0, method="mlsd", time_tag=True, delete=True):
    start_time = time.time()
    duration = 0
    i = 1
    while duration < interval or continuous:
        logger.info("子进程 - {0} 第{1}次执行".format(ftp_paras, i))
        ftp_client = FTPClient(ftp_para["host"], ftp_para["port"], ftp_para["user"], ftp_para["pwd"])
        ftp_client.connect()
        ftp_client.download(ftp_para["RemotePath"], ftp_para["LocalPath"], size_=size_,
                            method=method, time_tag=time_tag, delete=delete)
        time.sleep(300)
        duration = time.time() - start_time
        i = i+1


def run_task(ftp_paras, size_, method, time_tag):
    ftp_para = FTPParameters[ftp_paras]
    logger.info("子进程 - {0} 开始".format(ftp_paras))
    run_ftp(ftp_para, ftp_paras, continuous=True, size_=size_, method=method, time_tag=time_tag)
    logger.info("子进程 - {0} 结束".format(ftp_paras))


if __name__ == '__main__':
    logger.info("开始FTP自动化脚本")
    p = Pool(3)
    p.apply_async(run_task, args=("UELogToMgmt", 104816000, "nlst", False))
    p.apply_async(run_task, args=("UELogToArray", 104816000, "mlsd", True))
    p.apply_async(run_task, args=("eNBLogToArray", 31457000, "mlsd", True))
    logger.info("开启FTP子进程")
    p.close()
    p.join()
    logger.info("FTP自动化脚本关闭")

