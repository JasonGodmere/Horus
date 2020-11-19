
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
        if self.scope['user'].id:
            await self.send(text_data=json.dumps({
                'message': "hi",
            }))
        else:
            try:
                # user is not authenticated yet
                data = json.loads(text_data)
                if 'token' in data.keys():
                    token = data['token']
                    print(data['token'])
                    user = fetch_user_from_token(token)
                    self.scope['user'] = user

            except Exception as e:
                # Data is not valid, so close it.
                print(e)

        if not self.scope['user'].id:
            self.close()
