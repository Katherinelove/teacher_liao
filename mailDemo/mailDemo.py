# -*- coding: utf-8 -*-

""" send mails"""

__author__ = 'katherinelove'
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart,MIMEBase

import smtplib

def _format_addr(s):
    name, addr=parseaddr(s)
    #print(name,addr)
    return formataddr((Header(name,"utf-8").encode(),addr))


def MIMEtext():
    from_addr = input("From:")
    password = input("Password:")
    to_addr = input("To:")
    smtp_server = input("SMTP server:")
    # 构造正文对象
    msg = MIMEText("hello word,my name is zeng shuai", "plain", "utf-8")
    msg["From"] = _format_addr("Python lover <%s>" % from_addr)
    msg["To"] = _format_addr("kate <%s>" % to_addr)
    msg["Subject"] = Header("来自曾帅的问候。。。。。", "utf-8").encode()
    # 发送
    server = smtplib.SMTP(smtp_server, 25)  # 163服务器端口25
    # set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

def HTML():
    from_addr = input("From:")
    password = input("Password:")
    to_addr = input("To:")
    smtp_server = input("SMTP server:")

    msg=MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>',"html","utf-8")

    msg["From"]=_format_addr("zengshuai<%s>"%from_addr)
    msg["To"]=_format_addr("love<%s>"%to_addr)
    msg["Subject"]=Header("我的天","utf-8").encode()

    server=smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()

def image():
    from_addr = input("From:")
    password = input("Password:")
    to_addr = input("To:")
    smtp_server = input("SMTP server:")

    # msg = MIMEText('<html><body><h1>Hello</h1>' +
    #                '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    #                '</body></html>', "html", "utf-8")
    msg=MIMEMultipart()#最小部件
    msg["From"] = _format_addr("zengshuai<%s>" % from_addr)
    msg["To"] = _format_addr("love<%s>" % to_addr)
    msg["Subject"] = Header("我的天", "utf-8").encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
    with open(r"E:\teacher_liao\files\images\1.jpg","rb") as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime=MIMEBase("image","jpg",filename="1.jpg ")
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


if __name__ == '__main__':
    # MIMEtext()
    # HTML()
    image()