# Messing with consumers

from channels.generic.websocket import WebsocketConsumer

class TestConsummer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        """Create a test consummer."""
        super().__init__(*args, **kwargs)
        self.connected = {}

    def connect(self):
        """Add a user to the list of connected."""
        self.accept()
        self.send(text_data="[Welcome %s!]" % self.username)

    def receive(self, *, text_data):
        """Receive new data."""
        if text_data.startswith("/name"):
            self.username = text_data[5:].strip()
            self.send(text_data="[set your username to %s]" % self.username)
        else:
            self.send(text_data=self.username + ": " + text_data)

    def disconnect(self, message):
        """Delete a user from the list of connected."""

