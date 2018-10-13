# MK500端口控制参数
dstIP = '10.63.153.212'        # MK500管理主机地址
dstPort = 11111                # MK500软件接口端口
BoxIp = '192.168.0.15'         # 盒子地址
pdnIp = '20.0.73.90'           # pdn服务器地址
StartUeId = 0                  # 起始UE的序号
EndUeId = 39                   # 终止UE的序号

# 从盒子拉取日志到管理机FTP参数
BoxFTPHost = BoxIp             # 盒子地址
BoxFTPPort = 21                # 盒子FTP端口
BoxFTPUser = "root"            # 盒子FTP用户名
BoxFTPPwd = "root"             # 盒子FTP密码
BoxRemotePath = ''             # 盒子侧日志文件存储的FTP路径
MgmtLocalPath = ''             # 管理主机侧FTP存储位置

# 管理机拉取日志到存储机FTP参数
MgmtFTPHost = dstIP            # 管理主机地址
MgmtFTPPort = 21               # 管理主机FTP端口
MgmtFTPUser = "root"           # 管理主机FTP用户
MgmtFTPPwd = "root"            # 管理主机FTP密码
MgmtRemotePath = ''            # 管理主机日志存储的FTP路径
LocalPath = ''                 # 存储机FTP存储位置

# 预处理参数
CmacLogOutput = "H:/"
