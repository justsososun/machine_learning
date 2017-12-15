# --coding:utf-8--

from email.mime.text import MIMEText
import smtplib
from email.utils import formataddr
from email.header import Header

sender = user = 'justsososun@sina.com'
pwd = 'justsoso85401558'
smtpserver = 'smtp.sina.com'


def sendEmail(subject, msg, receiver):
    """

    :param subject:
    :param msg:
    :param receiver:
    :return:
    """

    # 构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype,传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['From'] = formataddr(['sender_nickname', sender])  # 显示发件人信息
    msg['To'] = formataddr(['receiver_nickname', receiver])  # 显示收件人信息
    msg['Subject'] = subject  # 邮件主题

    try:
        server = smtplib.SMTP(smtpserver, 25)    # 创建SMTP对象
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        # server.set_debuglevel(1)
        server.login(user, pwd)   # login()方法用来登录SMTP服务器

        # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        return True, "邮件发送成功!"

    except smtplib.SMTPException, e:
        return False, '邮件发送失败:%s' %e


def sendEmail2(receiver):
    """
    use
    (1) smtplib.SMTP()
    (2) server.connect(smtpserver, 25)
    connect to smtp server
    :param receiver:
    :return:
    """
    msg = MIMEText('hello justsososun, send by Python...', 'plain', 'utf-8')
    msg['From'] = formataddr(['sender_nickname', sender])  # 显示发件人信息
    msg['To'] = formataddr(['receiver_nickname', receiver])  # 显示收件人信息
    msg['Subject'] = 'ttt'  # 邮件主题
    server = smtplib.SMTP()
    server.connect(smtpserver, 25)

    # server.set_debuglevel(1)
    server.login(user, pwd)  # login()方法用来登录SMTP服务器

    # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


if __name__ == '__main__':

    receiver = ['justsososun@sina.com', 'justsososun@126.com']  # 收件人列表
    subject = 'My Test!'
    msg = 'hello,send by Python.....'
    status, output = sendEmail(subject, msg, receiver)
    if status:
        print 'Success！', output
    else:
        print 'Error!', output
    # sendEmail2(receiver)



