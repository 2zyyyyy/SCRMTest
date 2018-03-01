from HTMLTestRunner_PY3 import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import unittest
import time
import os


# ==========定义发送邮件==========
def send_mail(file_new):
    from_addr = 'xxxxxx@163.com'
    from_pass = 'xxxxxx'
    to_addr = 'xxxxxx@qq.com'
    smtp_server = 'smtp.163.com'

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # 发送的附件
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename= "report.html"'

    msg = MIMEMultipart('related')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = from_addr
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)
    smtp.login(from_addr, from_pass)
    smtp.sendmail(from_addr, to_addr, msg.as_string())
    smtp.quit()
    print('邮件已成功发送!')


# =====查找测试报告目录，找到最新生成的测试报告文件=====
def new_report(testReport):
    lists = os.listdir(testReport)
    lists.sort(key=lambda fn: os.path.getmtime(testReport + '\\' + fn))
    file_new = os.path.join(testReport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = './crm/report/' + now + 'result.html'
    fp = open(fileName, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='小旺猫后台管理系统自动化测试报告',
                            description='环境:Windows 10专业版\n浏览器:Google Chrome')
    discover = unittest.defaultTestLoader.discover('./crm/test_case', pattern='*_sta.py')
    runner.run(discover)
    fp.close()  # 关闭生成的报告
    file_path = new_report('./crm/report/')  # 查找新生成的报告
    send_mail(file_path)  # 调用发邮件模块
