# consumer를 routing 하는 곳
# django-channels는 연결 내용에 따라 디스패치할 컨슈머를 결합하고 쌓을 수 있는 라우팅 클래스를 제공한다.
# 비동기 애플리케이션을 위한 장고의 URL 라우팅 시스템이라고 생각하면 된다.
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(
        # django-channels URL 라우팅의 제한으로 인해 re_path 함수를 사용한다.
        # 각각의 사용자 연결에 대해 Consumer 인스턴스를
        # 인스턴스화 하는 Asgi Application을 얻기 위해 as_asgi() 클래스 메소들 호출한다
        # 이는 요청별 Django view instance에 대해 일한 역할을 수행하는 as_view()와 유사하다
        r"ws/chat/(?P<room_name>\w+)/$",
        consumers.ChatConsumer.as_asgi(),
    ),
]
