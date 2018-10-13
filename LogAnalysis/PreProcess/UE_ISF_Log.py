#模块导入
import pandas as pd
import re

#文件路径
FilePath = r"d:/data/"
OriginFile = FilePath + r"UE2LOG.txt"
UELogFixed = FilePath + r"UELogOutput.xlsx"

#文本匹配符
re_Date = r"(\d{4}\s\w{3,4}\s{2}\d\s{2}\d{2}\:\d{2}\:\d{2}\.\d{3})"

#读取文本日志并进行匹配分割
with open(OriginFile, "r") as rf:
    a = rf.read()
list_log = re.split(re_Date,a)

#分割字段提取packet中具体信息
DateTime = list_log[1::2]
list_log = list_log[2::2]
Unknown1 = [re.search(r"\[\w{2}\]", i).group() for i in list_log]
Type = [re.search(r"0x\w{4}", i).group() for i in list_log]
Description = [re.search(r"(?<=0x\w{4}  ).+(?=\n)", i).group() for i in list_log]
Length = [eval(re.search(r"(?<=Length:)\s*\d*(?=\n)", i).group()) for i in list_log]
Header = [re.search(r"(?<=Header:).*(?=\n)", i).group()[2:-1] for i in list_log]
Payload = [(i[re.search(r"(?<=Payload:).*(?=\n)", i).span()[0]:]).split("Payload:")[-1].replace("\n","").
           replace("\t","").replace("         ","")[1:-1] for i in list_log]
Message = ["".join(re.split((r"(\n)"),re.search(r".*(?=\n\tLength:)", i, re.DOTALL).group())[2:]) for i in list_log]

df_log = pd.DataFrame({"DateTime":DateTime,
                       "Unknown1":Unknown1,
                       "Type":Type,
                       "Description":Description,
                       "Length":Length,
                       "Header":Header,
                       "Payload":Payload,
                       "Message":Message})

df_log.to_excel(UELogFixed)