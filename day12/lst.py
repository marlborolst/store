from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.header import Header

send_user = '1054463446@qq.com'
send_password = 'nwnjhdqkdyabbfhb'# 本人邮件发送授权码
send_subject = '计算器'# 本次邮件发送的主题
send_file = open(r'D:\python\day12\代码\计算器.html', 'rb').read()

msg = MIMEText(send_file, 'base64', 'utf - 8')
# 邮件内容
msg['Content-Type'] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg['Content-Disposition'] = 'attachment;filename="jisuanqi.html"'
# 创建一个带附件的实例
msgRoot = MIMEMultipart('related')
msgRoot["From"] = Header("刘思彤", "utf-8")
msgRoot["TO"] = Header("j", "utf-8")
msgRoot['Subject'] = send_subject
msgRoot.attach(msg)

sendUser = '1054463446@qq.com'
receive = "2431320433@qq.com"

try:
    smt = smtplib.SMTP('smtp.qq.com')
    smt.ehlo()
    smt.starttls()
    smt.login(send_user, send_password)
    smt.sendmail(sendUser, receive, msgRoot.as_string())
    smt.quit()
    print('发送成功')
except Exception as e:
    print("发送失败")