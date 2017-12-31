import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
fund_list = pd.read_csv("e:/wenpeiyu/pythonproject/lianjiaspider/fundlist.csv")
fundcompany = "http://fund.cmbchina.com/FundPages/OpenFund/OpenFundDetail.aspx?Channel=Company&FundID={id_}"
fundoverview = "http://fund.cmbchina.com/FundPages/OpenFund/OpenFundDetail.aspx?Channel=Overview&FundID={id_}"
fund = "http://fund.cmbchina.com/FundPages/OpenFund/OpenFundDetail.aspx?&FundID={id_}"
funddetail = "http://live.cmbchina.com/FundHtmlBin/Html/{id_}.htm"
temp = pd.DataFrame()
for i in range(10):
    print(i)
    id_ = "%06d" %fund_list.iloc[i,0]
    company = fundcompany.format(id_=id_)
    overview = fundoverview.format(id_=id_)
    fund = fund.format(id_=id_)
    overviewinfo = pd.read_html(overview,encoding='utf-8')[0]
    overviewinfo = overviewinfo.transpose()
    mapping = {i[0]: i[1] for i in zip(range(20), list(overviewinfo.iloc[0,:]))}
    overviewinfo = overviewinfo.rename(columns = mapping ).drop(0)
    a = requests.get(funddetail.format(id_=id_))
    a.apparent_encoding
    a.encoding = 'GB2312'
    res = bs(a.text,"lxml")
    a = res.find_all("div", class_="content_Row")
    if a == []:
        temp = pd.concat([temp, overviewinfo])
    else:
        jijinjingli = a[3].find("a").string
        overviewinfo["基金经理"] = jijinjingli
        rengoufeilv = a[5].string.strip()
        overviewinfo["认购费率"] = rengoufeilv
        shengoufeilv = a[6].string.strip()
        overviewinfo["申购费率"] = shengoufeilv
        shuhuifeilv  = a[7].string.strip()
        overviewinfo["赎回费率"] = shuhuifeilv
        touzimubiao = a[8].string.strip()
        overviewinfo["投资目标"] = touzimubiao
        dangqianjingzhi = a[9].find_all("td")[0].string
        overviewinfo["当前净值"] = dangqianjingzhi
        leijijingzhi = a[9].find_all("td")[2].string
        overviewinfo["累计净值"] = leijijingzhi
        jingzhiriqi = a[9].find_all("td")[4].string
        overviewinfo["净值日期"] = jingzhiriqi
        rihuibao = a[9].find_all("td")[1].find("span").string
        overviewinfo["日回报"] = rihuibao
        rizhangdie = a[9].find_all("td")[3].find("span").string
        overviewinfo["日涨跌"] = rizhangdie
        zichanpeizhi = ""
        for i,j in enumerate(a[14].find_all("td")):
            if i % 2 == 0:
                zichanpeizhi = zichanpeizhi + j.string + "\t"
            else:
                zichanpeizhi = zichanpeizhi + j.string + "\n"
        overviewinfo["资产配置"] = zichanpeizhi
        hangyetouzizuhe = ""
        for i,j in enumerate(a[15].find_all("td")):
            if j.string == "--":
                continue
            if i % 2 == 0:
                hangyetouzizuhe = hangyetouzizuhe + j.string + "\t"
            else:
                hangyetouzizuhe = hangyetouzizuhe + j.string + "\n"
        overviewinfo["行业投资组合"] = hangyetouzizuhe
        temp = pd.concat([temp, overviewinfo])
temp.to_excel()