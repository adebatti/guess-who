# game/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_session_id = self.scope['url_route']['kwargs']['game_session_id']
        self.game_group_name = f'game_{self.game_session_id}'

        # Add the user to the game group
        await self.channel_layer.group_add(
            self.game_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the game group
        await self.channel_layer.group_discard(
            self.game_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming WebSocket data (not used in this example)
        pass

    async def game_message(self, event):
        # Send game-specific messages to the WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
