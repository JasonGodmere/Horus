
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login, logout

import json
import platform

class HubConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        print(self.user)

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
        '''text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )'''
        #system information

        uname = platform.uname()
        

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'diagnostics': [
                f"System: {uname.system}",
                f"Release: {uname.release}",
                f"Version: {uname.version}",
                f"Node Name: {uname.node}",
                f"Machine: {uname.machine}",
                f"Processor: {uname.processor}"
            ]
        }))


    # Diagnostics request for Horus Hub server
    async def d_request(self, event):

        #system information
        uname = platform.uname()
        

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'diagnostics': [
                f"System: {uname.system}",
                f"Node Name: {uname.node}",
                f"Release: {uname.release}",
                f"Version: {uname.version}",
                f"Machine: {uname.machine}",
                f"Processor: {uname.processor}"
            ]
        }))