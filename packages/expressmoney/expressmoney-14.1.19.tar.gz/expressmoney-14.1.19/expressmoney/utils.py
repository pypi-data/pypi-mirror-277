from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings


def get_client_ip(request):
    """Получить ip клиента из request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CurrentUserIdDefault:
    """Получить user_id из request для сериалайзера"""
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.id

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class ClientIpDefault:
    """Получить ip клиента из request для сериалайзера"""
    requires_context = True

    def __call__(self, serializer_field):
        return get_client_ip(serializer_field.context['request'])

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class PageSizePagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class CustomJWTAuthentication(JWTAuthentication):
    def get_header(self, request):
        """
        Для авторизации с заголовком: Proxy-Authorization: Bearer 8e2928a5f341513728ee6870c57652582a3af99c
        """
        if request.META.get('HTTP_PROXY_AUTHORIZATION'):
            header = request.META.get('HTTP_PROXY_AUTHORIZATION')
        else:
            header = request.META.get(api_settings.AUTH_HEADER_NAME)
        if isinstance(header, str):
            header = header.encode(HTTP_HEADER_ENCODING)
        return header
