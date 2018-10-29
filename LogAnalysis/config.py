# MK500端口控制参数
dstIP = '10.63.153.212'                 # MK500管理主机地址
dstPort = 11111                         # MK500软件接口端口
BoxIp = '192.168.0.9'                  # 盒子地址
pdnIp = '20.0.73.60'                    # pdn服务器地址

# FTP参数
FTPParameters = {
    # 从盒子拉取UE日志到管理机
    "UELogToMgmt": {
        "host": BoxIp, "port": 21, "user": "root", "pwd": "root",
        "RemotePath": "/home/root/temp/",
        "LocalPath": "D:/wenpeiyu/uelog/"
    },
    # 从管理机拉取UE日志到存储阵列
    "UELogToArray": {
        "host": dstIP, "port": 21, "user": "uelog", "pwd": "root",
        "RemotePath": "/",
        "LocalPath": "H:/LogAnalysis/RawData/MK500UELog/7/"
    },
    # 从管理机拉取基站日志到存储阵列
    "eNBLogToArray": {
        "host": dstIP, "port": 21, "user": "enblog", "pwd": "root",
        "RemotePath": "/",
        "LocalPath": "H:/LogAnalysis/RawData/eNodeBLog/7/"
    },
}

# 预处理参数
CmacLogInput = "H:/LogAnalysis/RawData/eNodeBLog/"
CmacLogOutput = "H:/LogAnalysis/RawData/eNodeBLog/output/"
