from utils import *
from log import logger


def _pre_cmac_log(input_path, output_path):
    """
    基站Cmac日志文件处理模块
    :param input_path: 原文件
    :param output_path: 输出路径
    """
    filename = os.path.basename(input_path).split(".")[0]
    output_path = os.path.join(output_path, filename + "_output.txt")
    if not os.path.exists(output_path):
        lines = open(input_path, encoding="utf-8").readlines()
        f = open(output_path, "a")
        cur_line = -1
        for lineInd in range(len(lines)):
            # 如果是行1，更新current行1
            if -1 != lines[lineInd].find("|||"):
                cur_line = lineInd
                # first = True
                continue
            elif cur_line == -1:
                continue
            # 如果不是行1，且有current行1，继续找行2
            # if first:
            res = lines[cur_line].split("|||")[0]
            res = res.split('Pri:')[1][3:]
            first = False
            # else:
            # res=' '*len(lines[curline].split("|||")[0])
            # 如果不是行2，continue继续找
            if -1 == lines[lineInd].find("||"):
                continue
            # 是行2，保存行2数据，然后找行3
            tmp = lines[lineInd].split('||')[0]
            res += tmp.split('Pri:')[1][3:]
            lineInd += 1
            if lineInd == len(lines):
                continue
            # 判断是否行3.如果找到了行1或行2，回退
            if -1 != lines[lineInd].find("|||") or -1 != lines[lineInd].find("||"):
                lineInd -= 1
                continue
            res = lines[lineInd].split('Pri:')[0] + 'Pri:' + \
                  lines[lineInd].split('Pri:')[1][:3] + res + \
                  lines[lineInd].split('Pri:')[1][3:]
            f.write(res)
        f.close()
        logger.info("{0}输出成功".format(filename))


def pre_cmac_log(input_path):
    """
    将原始CMAC日志文本转换为整齐格式的CMAC日志文本
    :param input_path: 原始日志存储目录
    :param output_path: 输出日志存储目录
    :return:
    """
    # 创建输出文件夹
    output_path = input_path + "/output/"
    try:
        os.makedirs(output_path)
        logger.info("文件夹{0}创建成功".format(output_path))
    except FileExistsError:
        logger.warn("文件夹{0}已存在".format(output_path))
    # 遍历文件夹生成原文件列表
    file_list = dir_list(input_path, "BPN((?!output).)*$")
    for i in file_list:
        _pre_cmac_log(i, output_path)


pre_cmac_log("H:/LogAnalysis/RawData/eNodeBLog/3/")
