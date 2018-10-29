from utils import *
from mk500 import MK500
from win32com.client import GetObject


def run_detach():
    client = MK500()
    client.detach(0, 149)
    time_sleep(45)
    client.clear()


def run_service():
    client = MK500()
    client.attach(0, 29)
    time_sleep(10)
    client.upload(0, 29)
    time_sleep(300)
    client.attach(30, 59)
    time_sleep(10)
    client.download(30, 59)
    time_sleep(300)
    client.attach(60, 89)
    time_sleep(10)
    client.pos(60, 89)
    time_sleep(300)
    client.attach(90, 119)
    time_sleep(10)
    client.danche(90, 119)
    time_sleep(300)
    client.attach(120, 149)
    time_sleep(10)
    client.shuibiao(120, 149)
    time_sleep(300)


def kill_pid(name):
    WMI = GetObject('winmgmts:')
    processes = WMI.InstancesOf('Win32_Process')
    process_list = [(p.Properties_("ProcessID").Value, p.Properties_("Name").Value) for p in processes]
    pid_list = [p[0] for p in process_list if name in p]
    for pid in pid_list:
        os.popen("taskkill /F /pid {0}".format(pid))


if __name__ == "__main__":
    while True:
        kill_pid("MK500.exe")
        kill_pid("java.exe")
        time_sleep(10)
        os.popen("D:\MK500\MK500_0921\MK500.exe")
        time_sleep(15)
        a = time.time()
        while time.time()-a < 10000:
            run_detach()
            run_service()
           
