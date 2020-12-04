from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from common import error
from lib.http import render_json
from user.models import User


class CorsMiddleware(MiddlewareMixin):
    """处理客户端 JS 的 跨域"""
    def process_request(self, request):
        if request.method == 'OPTIONS' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.Meta:
            response = HttpResponse()
            response['Content-length'] = '0'
            response['Access-Control-Allow-Headers'] = response.Meta['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']
            response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
            return response

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response


class AuthMiddleware(MiddlewareMixin):
    """用户登录验证中间件"""
    WHITE_LIST = [
        '/api/user/verify',
        '/api/user/login',
    ]

    def process_request(self, request):
        # 如果请求的URL在白名单内，直接跳过检查
        for path in self.WHITE_LIST:
            if request.path.startswith(path):
                return

        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
            except User.DoesNotExists:
                request.session.flush()
        return render_json(None, code=error.LOGIN_ERROR)