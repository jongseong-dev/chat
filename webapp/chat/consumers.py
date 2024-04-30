import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """
        새로운 연결이 수신될 때 호출된다.
        accept()를 호출하여 연결을 수락하거나 close()를 호출하여 거부할 수 있다.
        :return:
        """
        self.accept()

    def disconnect(self, close_code):
        """
        소켓이 닫힐 때 호출 된다. 클라이언트가 연결을 닫을 때 아무런 동작을 구현할 필요가 없으므로 Pass를 사용한다.
        :param close_code:
        :return:
        """
        pass

    def receive(self, text_data):
        """
        데이터가 수신될 때마다 호출된다.
        텍스트가 text_data로 수신된다고 전자한다.(바이너리 데이터의 경우 binary_data로 전달될 수 있음)
        self.send()를 사용해서 웹소켓으로 메시지를 돌려보낸다.
        :param text_data:
        :return:
        """
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))
