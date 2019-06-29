import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
from module.system import get_info


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def mail_format(content):
    msg = MIMEText("Hi, there!\n" + content + \
                   '\n\n(This email was sent by "Warframe-TennoCon2019 project" auto-send-email-system)\n' + \
                   '(此电子邮件由"Warframe-TennoCon2019 project"邮件自动发送系统发出)\n' + \
                   'POWERED BY SCTOP', "plain", "utf-8")
    return msg


class mail():
    def __init__(self, host, port, username, password):
        """

        :param host: 一个ip或者域名
        :param port: 端口，用于连接（必须是SSL端口，否则会失败）
        :param username: 一个列表两个内容，第一个是登录用用户名，第二个是邮箱地址
        :param password: SMTP/POP登录用密码（仅在本地存储）
        """
        self.__HOST__ = str(host)
        self.__HOSTPORT__ = int(port)
        self.__USERNAME__ = str(username[0])
        self.__PASSWORD__ = str(password)
        self.__SENDER__ = str(username[1])

    def send_mail(self, content):
        # 创建一个用于发送的对象
        content['From'] = _format_addr("TennoCon2019-AutoSystem<%s>" % self.__USERNAME__)
        content['To'] = _format_addr("Administrator <%s>" % self.__USERNAME__)
        content['Subject'] = Header('TennoCon2019 状态(status)', 'utf-8').encode()
        # 连接
        server = smtplib.SMTP_SSL(self.__HOST__, self.__HOSTPORT__)
        # server.starttls()
        server.set_debuglevel(1)
        # 登录并发送
        server.login(self.__USERNAME__, self.__PASSWORD__)
        server.sendmail(self.__SENDER__, self.__SENDER__, content.as_string())
        server.quit()


mail("smtp.qq.com", 465, ["2094880085", "2094880085@qq.com"], "aenroskqkmvtbjfj").send_mail(mail_format("111"))

# "aenroskqkmvtbjfj"
