"""
第三方配置
"""

# 互亿无线短信配置
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': 'C11649765',
    'password': '7b1212e90940aabaf2e9305ce997f8e8',
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile': None,
    'format': 'json'
}