# consumer를 routing 하는 곳
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(
        "ws/chat/<str:room_name>/",
        # 각각의 사용자 연결에 대해 Consumer 인스턴스를
        # 인스턴스화 하는 Asgi Application을 얻기 위해 as_asgi() 클래스 메소들 호출한다
        # 이는 요청별 Django view instance에 대해 일한 역할을 수행하는 as_view()와 유사하다
        consumers.ChatConsumer.as_asgi(),
    ),
]
