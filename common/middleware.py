from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


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



