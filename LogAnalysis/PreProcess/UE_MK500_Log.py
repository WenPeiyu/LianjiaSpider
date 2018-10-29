import pandas as pd
import re

FilePath = r"d:/data/"
OriginFile = FilePath + r"ueL2log5201810221749.txt"
LogOutput = FilePath + r"ueLogOutput.xlsx"
with open(OriginFile, encoding="utf-8") as f:
    lines = f.readlines()

re_UL = re.compile("ULMAC")
re_DL = re.compile("DLMAC")
re_HSFN = re.compile(r"(?<=HSFN:)\d+")
re_UEindex = re.compile(r"(?<=UeIndex:)\d+")
re_RNTI = re.compile(r"(?<=Rnti:)\d+")
re_sign = re.compile(r"\[[\w ]+\]")
re_MSG = re.compile(r"MSG")

DateTime = [i[1:13] for i in lines]
ULMAC = [1 if re_UL.search(i) else 0 for i in lines]
DLMAC = [1 if re_UL.search(i) else 0 for i in lines]
HSFN = [re_HSFN.search(i).group() if re_HSFN.search(i) else "***" for i in lines]
UEIndex = [re_UEindex.search(i).group() if re_UEindex.search(i) else "***" for i in lines]
RNTI = [re_RNTI.search(i).group() if re_RNTI.search(i) else "***" for i in lines]
lines = [("]").join(i.split("]")[4:]) if re_HSFN.search(i) else ("]").join(i.split("]")[3:]) for i in lines]
lines = [("]").join(i.split("]")[1:]) if (re_UEindex.search(i) and re_RNTI.search(i)) else ("]").join(i.split("]")) for i in lines]

sign = [re_sign.match(i).group() if re_sign.match(i) else "***" for i in lines]
MSG = [1 if re_MSG.search(i) else 0 for i in lines]
lines = [("]").join(i.split("]")[1:]) if (re_sign.search(i) and re_sign.search(i)) else ("]").join(i.split("]")) for i in lines]

df_log = pd.DataFrame({"DateTime": DateTime,
                       "ULMAC": ULMAC,
                       "DLMAC": DLMAC,
                       "HSFN": HSFN,
                       "RNTI": RNTI,
                       "UEIndex": UEIndex,
                       "Sign": sign,
                       "MSG": MSG,
                       "message": lines
                      })
df_log.to_excel(LogOutput)