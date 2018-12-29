import os
import re
import time
import mysql.connector
from multiprocessing import Pool
import pandas as pd
from log import logger


def dir_list(path, filter_=None, dir_=False):
    """
    获得路径的所有文件列表
    :param path: 目标路径
    :param filter_: 过滤器（正则表达式） 默认不开启
    :param dir_: 文件夹开关 True:返回结果包含文件夹 False:返回结果不含文件夹
    :return: list
    """
    file_list = []
    # 判断文件夹是否可读
    try:
        os.chdir(path)
    except PermissionError:
        return None
    # 展开文件夹做循环
    for i in os.listdir(path):
        # 利用正则表达式做筛选
        if filter_ is None:
            boolean_filter = True
        else:
            ignore_pattern = re.compile(filter_)
            if ignore_pattern.match(i):
                boolean_filter = True
            else:
                boolean_filter = False
        current_path = os.path.join(path, i)
        # 若当前文件项是文件则放入输出列表中
        if os.path.isfile(current_path):
            if not boolean_filter:
                continue
            file_list.append(current_path)
        # 若当前文件项是文件夹则递归循环本函数
        elif os.path.isdir(current_path):
            try:
                if dir_:
                    file_list.append(current_path)
                file_list = file_list + dir_list(current_path, filter_, dir_)
            except TypeError:
                pass
    return file_list


lstdir = dir_list(r"G:\20180723-26\test2325", filter_="LTE", dir_=True)
lstdir = lstdir + dir_list(r"G:\20180723-26\test26", filter_="LTE", dir_=True)
config = {
    'host': 'localhost',
    'port': 3310,
    'user': 'root',
    'password': 'ASDF-1234',
    'database': 'mrenodeb',
    'charset': 'utf8'
}
lstfile = [lstdir[i * 400:(i + 1) * 400 - 1] for i in range(10)]

str_table_create = '''create table table_{tablename}
(
  `Key`                           text null,
  eNodeBID                        text null,
  CID                             text null,
  TraceID                         text null,
  PCI                             text null,
  IMSI                            text null,
  IMEI                            text null,
  MeasTime                        text null,
  RSRP                            text null,
  RSRQ                            text null,
  Day                             text null,
  Hour                            text null,
  `MR Lon`                        text null,
  `MR Lat`                        text null,
  DataType                        text null,
  PHR                             text null,
  RIP                             text null,
  ULMCS                           text null,
  DLMCS                           text null,
  ULSINR                          text null,
  ULBLER                          text null,
  TxPower                         text null,
  TA                              text null,
  Earth_X                         text null,
  Earth_Y                         text null,
  EarthID                         text null,
  MilliSec                        text null,
  Network                         text null,
  UEGid                           text null,
  CallRecordUEID                  text null,
  AoA                             text null,
  RecvBsr                         text null,
  PuschPrbNum                     text null,
  PdschPrbNum                     text null,
  UlErabSetupPresent              text null,
  LocationType                    text null,
  DataErabUlPdcpTput              text null,
  DataErabDLPdcpTput              text null,
  DmacUlFlowRate                  text null,
  DmacDlFlowRate                  text null,
  PdschDtxCtn                     text null,
  DlRsTxPower                     text null,
  ThermalNoisePower               text null,
  ServerCellEarfcn                text null,
  NeighCellNum                    text null,
  NCellEarfcn                     text null,
  NeighCellENBID                  text null,
  NeighCellID                     text null,
  NeighPCI                        text null,
  NeighCellRSRP                   text null,
  NeighCellRSRQ                   text null,
  NeighFlag                       text null,
  DLTM                            text null,
  PdschSingleFlowAveMcs           text null,
  PdschDoubleFlow1AveMcs          text null,
  PdschDoubleFlow2AveMcs          text null,
  PuschAveMcs                     text null,
  Cqi0                            text null,
  Cqi1                            text null,
  BeforeTherotySINR               text null,
  MMEC                            text null,
  MMEApID                         text null,
  MMEGroupID                      text null,
  PositionMark                    text null,
  PdschAckCtn                     text null,
  PdschNackCtn                    text null,
  PositionNBRSize                 text null,
  StrongestRSRP                   text null,
  StrongestNBPCI                  text null,
  Grid_THREE_COLUMN_10            text null,
  Grid_THREE_COLUMN_20            text null,
  Grid_THREE_COLUMN_50            text null,
  Grid_THREE_COLUMN_100           text null,
  Grid_THREE_COLUMN_200           text null,
  HighSpeedUserStatus             text null,
  PuschAckCtn                     text null,
  PuschNackCtn                    text null,
  ULPLR                           text null,
  DLPLR                           text null,
  AllErabUlPdcpTput               text null,
  AllErabDLPdcpTput               text null,
  Flag                            text null,
  TaDltValue                      text null,
  SupperCellType                  text null,
  SupperCellCpId                  text null,
  IntraNeighTotalPower            text null,
  PuschUsePrbNum                  text null,
  PdschUsePrbNum                  text null,
  PuschAvailPrbNum                text null,
  PdschAvailPrbNum                text null,
  ULPdcpValidTimerLen             text null,
  DLPdcpValidTimerLen             text null,
  DLTmCtn                         text null,
  ReportCellName                  text null,
  DLRB                            text null,
  ULRB                            text null,
  SumUeTputUlPdcpWithoutLastPiece text null,
  SumUeTputDlPdcpWithoutLastPiece text null,
  SumUeTputPuschPrbNum            text null,
  SumUeTputPdschPrbNum            text null,
  SpId                            text null,
  TerminalID                      text null,
  UtranCellUarfcn                 text null,
  UtranCellRSCP                   text null,
  UtranCellEcIO                   text null,
  GsmArfcn                        text null,
  GsmRssi                         text null,
  CdmaArfcn                       text null,
  CdmapilotStrength               text null,
  ReportCellKey                   text null,
  UlPathLoss                      text null,
  CCEAlloCnt_1                    text null,
  CCEAlloCnt_2                    text null,
  CCEAlloCnt_4                    text null,
  CCEAlloCnt_8                    text null,
  ReportRI1                       text null,
  ReportRI2                       text null,
  ReportRI4                       text null,
  ReportRI8                       text null,
  LTEInterUarfcn                  text null,
  LTEInterRsrp                    text null,
  GnssLocationType                text null,
  GNSSLocationInfo                text null,
  earthx                          text null,
  earthy                          text null,
  MTMSI                           text null,
  TAResult                        text null,
  RRUID                           text null,
  CRNTI                           text null,
  cDoaAngleTheta                  text null,
  cDoaAnglePhi                    text null,
  floor                           text null,
  buildingid                      text null
);'''


str_insert = '''insert into {tablename} (`Key`,eNodeBID,CID,TraceID,PCI,IMSI,IMEI,MeasTime,RSRP,RSRQ,Day,Hour,`MR Lon`,`MR Lat`,DataType,PHR,RIP,ULMCS,DLMCS,ULSINR,ULBLER,TxPower,TA,Earth_X,Earth_Y,EarthID,MilliSec,Network,UEGid,CallRecordUEID,AoA,RecvBsr,PuschPrbNum,PdschPrbNum,UlErabSetupPresent,LocationType,DataErabUlPdcpTput,DataErabDLPdcpTput,DmacUlFlowRate,DmacDlFlowRate,PdschDtxCtn,DlRsTxPower,ThermalNoisePower,ServerCellEarfcn,NeighCellNum,NCellEarfcn,NeighCellENBID,NeighCellID,NeighPCI,NeighCellRSRP,NeighCellRSRQ,NeighFlag,DLTM,PdschSingleFlowAveMcs,PdschDoubleFlow1AveMcs,PdschDoubleFlow2AveMcs,PuschAveMcs,Cqi0,Cqi1,BeforeTherotySINR,MMEC,MMEApID,MMEGroupID,PositionMark,PdschAckCtn,PdschNackCtn,PositionNBRSize,StrongestRSRP,StrongestNBPCI,Grid_THREE_COLUMN_10,Grid_THREE_COLUMN_20,Grid_THREE_COLUMN_50,Grid_THREE_COLUMN_100,Grid_THREE_COLUMN_200,HighSpeedUserStatus,PuschAckCtn,PuschNackCtn,ULPLR,DLPLR,AllErabUlPdcpTput,AllErabDLPdcpTput,Flag,TaDltValue,SupperCellType,SupperCellCpId,IntraNeighTotalPower,PuschUsePrbNum,PdschUsePrbNum,PuschAvailPrbNum,PdschAvailPrbNum,ULPdcpValidTimerLen,DLPdcpValidTimerLen,DLTmCtn,ReportCellName,DLRB,ULRB,SumUeTputUlPdcpWithoutLastPiece,SumUeTputDlPdcpWithoutLastPiece,SumUeTputPuschPrbNum,SumUeTputPdschPrbNum,SpId,TerminalID,UtranCellUarfcn,UtranCellRSCP,UtranCellEcIO,GsmArfcn,GsmRssi,CdmaArfcn,CdmapilotStrength,ReportCellKey,UlPathLoss,CCEAlloCnt_1,CCEAlloCnt_2,CCEAlloCnt_4,CCEAlloCnt_8,ReportRI1,ReportRI2,ReportRI4,ReportRI8,LTEInterUarfcn,LTEInterRsrp,GnssLocationType,GNSSLocationInfo,earthx,earthy,MTMSI,TAResult,RRUID,CRNTI,cDoaAngleTheta,cDoaAnglePhi,floor,buildingid) value ("{Key}","{eNodeBID}","{CID}","{TraceID}","{PCI}","{IMSI}","{IMEI}","{MeasTime}","{RSRP}","{RSRQ}","{Day}","{Hour}","{MR Lon}","{MR Lat}","{DataType}","{PHR}","{RIP}","{ULMCS}","{DLMCS}","{ULSINR}","{ULBLER}","{TxPower}","{TA}","{Earth_X}","{Earth_Y}","{EarthID}","{MilliSec}","{Network}","{UEGid}","{CallRecordUEID}","{AoA}","{RecvBsr}","{PuschPrbNum}","{PdschPrbNum}","{UlErabSetupPresent}","{LocationType}","{DataErabUlPdcpTput}","{DataErabDLPdcpTput}","{DmacUlFlowRate}","{DmacDlFlowRate}","{PdschDtxCtn}","{DlRsTxPower}","{ThermalNoisePower}","{ServerCellEarfcn}","{NeighCellNum}","{NCellEarfcn}","{NeighCellENBID}","{NeighCellID}","{NeighPCI}","{NeighCellRSRP}","{NeighCellRSRQ}","{NeighFlag}","{DLTM}","{PdschSingleFlowAveMcs}","{PdschDoubleFlow1AveMcs}","{PdschDoubleFlow2AveMcs}","{PuschAveMcs}","{Cqi0}","{Cqi1}","{BeforeTherotySINR}","{MMEC}","{MMEApID}","{MMEGroupID}","{PositionMark}","{PdschAckCtn}","{PdschNackCtn}","{PositionNBRSize}","{StrongestRSRP}","{StrongestNBPCI}","{Grid_THREE_COLUMN_10}","{Grid_THREE_COLUMN_20}","{Grid_THREE_COLUMN_50}","{Grid_THREE_COLUMN_100}","{Grid_THREE_COLUMN_200}","{HighSpeedUserStatus}","{PuschAckCtn}","{PuschNackCtn}","{ULPLR}","{DLPLR}","{AllErabUlPdcpTput}","{AllErabDLPdcpTput}","{Flag}","{TaDltValue}","{SupperCellType}","{SupperCellCpId}","{IntraNeighTotalPower}","{PuschUsePrbNum}","{PdschUsePrbNum}","{PuschAvailPrbNum}","{PdschAvailPrbNum}","{ULPdcpValidTimerLen}","{DLPdcpValidTimerLen}","{DLTmCtn}","{ReportCellName}","{DLRB}","{ULRB}","{SumUeTputUlPdcpWithoutLastPiece}","{SumUeTputDlPdcpWithoutLastPiece}","{SumUeTputPuschPrbNum}","{SumUeTputPdschPrbNum}","{SpId}","{TerminalID}","{UtranCellUarfcn}","{UtranCellRSCP}","{UtranCellEcIO}","{GsmArfcn}","{GsmRssi}","{CdmaArfcn}","{CdmapilotStrength}","{ReportCellKey}","{UlPathLoss}","{CCEAlloCnt_1}","{CCEAlloCnt_2}","{CCEAlloCnt_4}","{CCEAlloCnt_8}","{ReportRI1}","{ReportRI2}","{ReportRI4}","{ReportRI8}","{LTEInterUarfcn}","{LTEInterRsrp}","{GnssLocationType}","{GNSSLocationInfo}","{earthx}","{earthy}","{MTMSI}","{TAResult}","{RRUID}","{CRNTI}","{cDoaAngleTheta}","{cDoaAnglePhi}","{floor}","{buildingid}")'''

lst_enodeb = list(pd.read_csv(r"C:\Users\wenpeiyu\Desktop\mr_enodebid_cid.csv")["enodeb"])


def createtable():
    for i in lst_enodeb:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(str_table_create.format(tablename=i))


def insertMR(path):
    lst_header = ["Key","eNodeBID","CID","TraceID","PCI","IMSI","IMEI","MeasTime","RSRP","RSRQ","Day","Hour","MR Lon","MR Lat","DataType","PHR","RIP","ULMCS","DLMCS","ULSINR","ULBLER","TxPower","TA","Earth_X","Earth_Y","EarthID","MilliSec","Network","UEGid","CallRecordUEID","AoA","RecvBsr","PuschPrbNum","PdschPrbNum","UlErabSetupPresent","LocationType","DataErabUlPdcpTput","DataErabDLPdcpTput","DmacUlFlowRate","DmacDlFlowRate","PdschDtxCtn","DlRsTxPower","ThermalNoisePower","ServerCellEarfcn","NeighCellNum","NCellEarfcn","NeighCellENBID","NeighCellID","NeighPCI","NeighCellRSRP","NeighCellRSRQ","NeighFlag","DLTM","PdschSingleFlowAveMcs","PdschDoubleFlow1AveMcs","PdschDoubleFlow2AveMcs","PuschAveMcs","Cqi0","Cqi1","BeforeTherotySINR","MMEC","MMEApID","MMEGroupID","PositionMark","PdschAckCtn","PdschNackCtn","PositionNBRSize","StrongestRSRP","StrongestNBPCI","Grid_THREE_COLUMN_10","Grid_THREE_COLUMN_20","Grid_THREE_COLUMN_50","Grid_THREE_COLUMN_100","Grid_THREE_COLUMN_200","HighSpeedUserStatus","PuschAckCtn","PuschNackCtn","ULPLR","DLPLR","AllErabUlPdcpTput","AllErabDLPdcpTput","Flag","TaDltValue","SupperCellType","SupperCellCpId","IntraNeighTotalPower","PuschUsePrbNum","PdschUsePrbNum","PuschAvailPrbNum","PdschAvailPrbNum","ULPdcpValidTimerLen","DLPdcpValidTimerLen","DLTmCtn","ReportCellName","DLRB","ULRB","SumUeTputUlPdcpWithoutLastPiece","SumUeTputDlPdcpWithoutLastPiece","SumUeTputPuschPrbNum","SumUeTputPdschPrbNum","SpId","TerminalID","UtranCellUarfcn","UtranCellRSCP","UtranCellEcIO","GsmArfcn","GsmRssi","CdmaArfcn","CdmapilotStrength","ReportCellKey","UlPathLoss","CCEAlloCnt_1","CCEAlloCnt_2","CCEAlloCnt_4","CCEAlloCnt_8","ReportRI1","ReportRI2","ReportRI4","ReportRI8","LTEInterUarfcn","LTEInterRsrp","GnssLocationType","GNSSLocationInfo","earthx","earthy","MTMSI","TAResult","RRUID","CRNTI","cDoaAngleTheta","cDoaAnglePhi","floor","buildingid"]
    dict_header = {i: lst_header[i] for i in range(133)}
    temp = pd.read_csv(path, header=None)
    temp = temp.rename(columns=dict_header)
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    start = time.time()
    for i in range(temp.shape[0]):
        a = dict(temp.iloc[i, :])
        sql_insert = str_insert.format(tablename="table_{tablename}".format(tablename=a["eNodeBID"]),  **a).replace('"nan"','NULL')
        try:
            cursor.execute(sql_insert)
            if i % 5000 == 0:
                print(i, time.time() - start)
                cnx.commit()

        except mysql.connector.Error as e:
            print('insert datas error!{}'.format(e))
    cursor.close()
    cnx.close()

# createtable()

# insertMR(r'G:\20180723-26\test2325\LTE_CDT_T054_DETAIL_169451_V1740_201807232330_1.csv')


def func(msg):
    insertMR(msg)
    logger.error(msg)


if __name__ == "__main__":
    pool = Pool(processes=20)
    for i in lstdir:
        pool.apply_async(func, (i, ))

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()    # behind close() or terminate()
    print("Sub-process(es) done.")
