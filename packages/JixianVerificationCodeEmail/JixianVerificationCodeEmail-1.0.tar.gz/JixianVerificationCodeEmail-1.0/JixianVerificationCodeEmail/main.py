import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string


def generate_verification_code(length=6):
    """生成随机验证码"""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def send_verification_code(email_to, smtp_server, smtp_port, username, password):
    """
    发送验证码至指定邮箱
    :param email_to: 收件人邮箱地址
    :param smtp_server: SMTP服务器地址
    :param smtp_port: SMTP服务器端口
    :param username: SMTP登录用户名
    :param password: SMTP登录密码
    :return: 发送成功返回验证码，否则返回None
    """
    verification_code = generate_verification_code()

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = email_to
    msg['Subject'] = "Your Verification Code"

    body = f"Your verification code is: {verification_code}. Please keep it safe."
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 如果SMTP服务器需要TLS安全连接
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        return verification_code
    except Exception as e:
        print(f"Failed to send email: {e}")
        return None


class Send_Verification_Code_Email:
    def __init__(self, smtp_server, username, password, smtp_port=25):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send(self, email_to):
        code = send_verification_code(email_to, self.smtp_server, self.smtp_port, self.username, self.password)
        if code:
            return code
        else:
            return "null"
