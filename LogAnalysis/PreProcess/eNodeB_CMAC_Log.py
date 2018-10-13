#导入模块
import pandas as pd
import re
import time

#路径地址
FilePath = r"d:/data/"
OriginFile = FilePath + r"BPN_3_40_multi_80_PBH_00_0_output.txt"
FixedCSV = FilePath + r"Fixed.csv"
ErrorFile = FilePath + r"Error.txt"
LogOutput = FilePath + r"LogOutput.xlsx"

time1 = time.time()
#读取文本转换成不存在歧义的CSV
with open(OriginFile, 'r') as f, open(FixedCSV, "w") as csv, open(ErrorFile, "w") as txt:
    a = True
    csv.write("")
    while a != [""]:
        a = f.readline()
        a = a.split("  ")
        try:
            a[8]="".join(a[8:])
            csv.write(";;;;".join(a[0:9]))
        except:
            txt.write(";;;;".join(a))

time2 = time.time()
#文本匹配符
re_I = re.compile(r"\[I\]")
re_U = re.compile(r"\[U\]")
re_D = re.compile(r"\[D\]")
re_RA = re.compile(r"\[RA\]")
re_TOOL = re.compile(r"\[TOOL\]")
re_MSG = re.compile(r"MSG")

time3 = time.time()
#读取CSV分割字段
df_log = pd.read_csv(FixedCSV, sep=";;;;", header=None)
DateTime = df_log.loc[:,0]
Sequence = df_log.loc[:,1]
LogSpace = df_log.loc[:,2]
PriClass = df_log.loc[:,3]
interHSFN = [eval(i)[0] for i in list(df_log.loc[:,4])]
sysHSFN = [i[1:-1].split(".")[0] for i in list(df_log.loc[:,5])]
SysFraNum = [i[1:-1].split(".")[1] for i in list(df_log.loc[:,5])]
SysSubFN = [i[1:-1].split(".")[2] for i in list(df_log.loc[:,5])]
PhyCellIdentifier = [i[1:-1].split(":")[0] for i in list(df_log.loc[:,6])]
CELs = [i[1:-1].split(":")[2] for i in list(df_log.loc[:,6])]
UEIndex = [i[1:-1].split(":")[0] for i in list(df_log.loc[:,7])]
CRNTI = [i[1:-1].split(":")[1] for i in list(df_log.loc[:,7])]
GID = [i[1:-1].split(":")[2] for i in list(df_log.loc[:,7])]
Message = df_log.loc[:,8]

time4 = time.time()
#分割日志信息体进行标注
I = [1 if re_I.match(i) else 0 for i in Message]
U = [1 if re_U.match(i) else 0 for i in Message]
D = [1 if re_D.match(i) else 0 for i in Message]
TOOL = [1 if re_TOOL.match(i) else 0 for i in Message]
RA = [1 if re_RA.search(i) else 0 for i in Message]
MSG = [1 if re_MSG.search(i) else 0 for i in Message]

df_log = pd.DataFrame({"DateTime":DateTime,
                       "Sequence":Sequence,
                       "LogSpace":LogSpace,
                       "PriClass":PriClass,
                       "interHSFN":interHSFN,
                       "sysHSFN":sysHSFN,
                       "SysFraNum":SysFraNum,
                       "SysSubFN":SysSubFN,
                       "PhyCellIdentifier":PhyCellIdentifier,
                       "CELs":CELs,
                       "UEIndex":UEIndex,
                       "CRNTI":CRNTI,
                       "GID":GID,
                       "I":I,
                       "U":U,
                       "D":D,
                       "TOOL":TOOL,
                       "RA":RA,
                       "MSG":MSG,
                       "Message":Message
                      })
time5 = time.time()
df_log.to_excel(LogOutput)
time6 = time.time()
RunTime = [time1, time2, time3, time4, time5, time6]