import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

from chat.routing import websocket_urlpatterns

# 이 루트 라우팅 구성은 채널 개발 서버에 연결될 때 ProtocolTypeRouter이 먼저 연결 유형을 검사하도록 지정합니다.
# WebSocket 연결(ws:// 또는 wss://)인 경우 AuthMiddlewareStack에 연결이 제공됩니다.
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            # AuthMiddlewareStack은 Django의 AuthenticationMiddleware이
            # 현재 인증된 사용자로 뷰 함수의 요청 객체를 채우는 방법과
            # 유사하게 현재 인증된 사용자에 대한 참조로 연결 범위를 채웁니다.
            # 그런 다음 URLRouter에 연결이 제공됩니다.
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)
