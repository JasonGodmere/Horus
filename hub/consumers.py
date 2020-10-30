
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login, logout

import json
import platform

class HubConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        '''
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )'''

    # Receive message from WebSocket
    async def receive(self, text_data):
        
        await self.send(text_data=json.dumps({
            'message': json.loads(text_data),
        }))
