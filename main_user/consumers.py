from channels.generic.websocket import AsyncWebsocketConsumer #handling websocket connection
import json
from channels.layers import get_channel_layer

#get channel layer
channel_layer = get_channel_layer()
channel_name = "shape_user"


#consumer to set up websocket
class ShapeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'public_room'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    
    #when django receives a websocket connection from client
    async def send_created_shape(self, event):
        await self.send(text_data=json.dumps({ 'shape': event}))
        
    async def send_deleted_shape(self, event):
        await self.send(text_data=json.dumps({ 'shape': event}))

    async def send_updated_shape(self, event):
        await self.send(text_data=json.dumps({ 'shape': event}))
