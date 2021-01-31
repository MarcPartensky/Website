# chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class EditorConsumer(WebsocketConsumer):
    """Deal with a consumer"""

    def connect(self):
        """Deal with the connection of a new user."""
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'code_%s' % self.room_name
        print(self.room_name)
        print(self.room_group_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """Deal with the connection of a new user."""
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        """Receive a websocket message."""
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('receiving:', message)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'code_message',
                'message': message
            }
        )

    # Receive message from room group
    def code_message(self, event):
        """Receive a message from the room group."""
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
