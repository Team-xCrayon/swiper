from user.logic import send_verify_code
from lib.http import render_json


# Create your views here.
def get_verity_code(request):
    """手机注册"""
    phonenum = request.Post.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None, 0)


def login(request):
    """短信验证登录"""
    pass


def get_profile(request):
    """获取个人资料"""
    pass


def modify_profile(request):
    """修改个人资料"""
    pass


def upload_avatar(request):
    """头像上传"""
    pass