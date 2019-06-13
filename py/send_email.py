import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_mail(smtp_server, sender, password, receiver, subject, content):
    """

    :param smtp_server: 邮箱的服务器，腾讯企业邮箱的为'smtp.exmail.qq.com'
    :param sender: 发送人
    :param password: 发送人的邮箱密码
    :param receiver: 接收人，多个用`,`隔开。 e.g: 'user1@qq.com,user2@qq.com'
    :param subject: 主题
    :param content: 内容
    :return:
    """
    msg_root = MIMEMultipart('related')
    msg_root['Subject'] = subject
    msg_root["From"] = sender
    msg_root["To"] = receiver
    msg_text = MIMEText(content, 'html', 'utf-8')
    msg_root.attach(msg_text)
    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)
    if len(password)>0:
        smtp.login(username, password)
    msg = smtp.sendmail(sender, receiver.split(','), msg_root.as_string())
    smtp.quit()
    return msg

if __name__ == '__main__':
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_USERNAMA = "haha@qudian.com"
    MAIL_PASSWORD = ""
    email = '972237007@qq.com'
    title = 'TESTI TITLE'
    content = 'ASFADSF'
    sendmail_html(MAIL_SERVER, MAIL_USERNAMA, MAIL_PASSWORD, email, title, content)
