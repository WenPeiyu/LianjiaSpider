import logging
from logging import handlers
import sys
import os

# 模块名称
ModuleName = "LogAnalysis"

# 打印文件日志生效地址
LogName = os.path.expanduser('~') + "/" + ModuleName + ".log"

# 日志格式
formatter = logging.Formatter('[%(asctime)s] - [%(filename)s][%(funcName)s][line:%(lineno)d]'
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
    ['wen.peiyu@zte.com.cn', 'me@wenpeiyu.com', 'bu.fanjie@zte.com.cn'],
    "logging from my app",
    credentials=('dxxxhly@163.com', '455190881451975'),
)
mail_handler.setFormatter(formatter)
mail_handler.setLevel(logging.ERROR)


class OptmizedMemoryHandler(handlers.MemoryHandler):
    def __init__(self, capacity, mail_subject, mail_host, mail_from, mail_to):
        """ capacity: flush memory
            mail_subject: warning mail subject
            mail_host: the email host used
            mail_from: address send from; str
            mail_to: address send to; multi-addresses splitted by ';'

        """
        handlers.MemoryHandler.__init__(self, capacity, flushLevel=logging.ERROR, \
                                                target=None)
        self.mail_subject = mail_subject
        self.mail_host = mail_host
        self.mail_from = mail_from
        self.mail_to = mail_to

    def flush(self):
        """if flushed send mail
        """
        if self.buffer != [] and len(self.buffer) >= self.capacity:
            content = ''
            for record in self.buffer:
                message = record.getMessage()
                content += record.levelname + " occurred at " + time.strftime('%Y-%m-%d %H:%M:%S', time.localti
                me(record.created)) + "  : " + message + '\n'
            self.send_warning_mail(self.mail_subject, content, self.mail_host, self.mail_from, self.mail_to)
            self.buffer = []

    def send_warning_mail(self, subject, content, host, from_addr, to_addr):
        """send mail
        """
        msg = MIMEText(content)
        msg['Subject'] = subject
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.sendmail(from_addr, to_addr, msg.as_string())
            smtp.close()
        except:
            print
            traceback.format_exc()


memory_handler = handlers.MemoryHandler(100)
memory_handler.setFormatter(formatter)
memory_handler.setLevel(logging.ERROR)
memory_handler.setTarget(mail_handler)


# 添加Handler生效
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(memory_handler)

logger.error("error")
logger.info("info")
logger.debug("debug")
logger.warning("warning")
logger.critical("critical")
