import logging
from logging import handlers
import sys
import os

# 模块名称
ModuleName = "MysqlInsert"

# 打印文件日志生效地址
LogName = os.path.expanduser('~') + "/" + ModuleName + ".log"

# 日志格式
formatter = logging.Formatter('[%(asctime)s] - [%(filename)s][%(funcName)s][%(process)d][line:%(lineno)d]'
                              ' - [%(levelname)s]: %(message)s')

# 日志初始化
logger = logging.getLogger(ModuleName)
logger.setLevel(logging.DEBUG)


# 文件日志Handler
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)
file_handler = logging.FileHandler(LogName, encoding='utf-8')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# 控制台日志Handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)

# 邮件日志Handler
mail_handler = handlers.SMTPHandler(
    ("smtp.163.com", 25), 'dxxxhly@163.com',
    ['wen.peiyu@zte.com.cn', 'me@wenpeiyu.com'],
    "logging from my app",
    credentials=('dxxxhly@163.com', ""),
)
mail_handler.setFormatter(formatter)
mail_handler.setLevel(logging.ERROR)

memory_handler = handlers.MemoryHandler(100)
memory_handler.setFormatter(formatter)
memory_handler.setLevel(logging.ERROR)
memory_handler.setTarget(mail_handler)

# 添加Handler生效
logger.addHandler(console_handler)
logger.addHandler(file_handler)
# logger.addHandler(memory_handler)
