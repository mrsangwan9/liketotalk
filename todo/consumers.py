import json
from .models import MyUser
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
 # that page handle server movement with handlers what the server will response.


class myasyncconsumer(AsyncWebsocketConsumer):
    async def connect(self):
          my_id= self.scope['user'].id
          other_id = self.scope['url_route']['kwargs']['other_id']
          print(my_id,other_id)
          if int(my_id)> int(other_id):
              self.room_name = f'{my_id}-{other_id}'
          else:
              self.room_name= f'{other_id}-{my_id}'
            
          self.room_group_name = 'chat_%s' % self.room_name

          await self.channel_layer.group_add(
              self.room_group_name,
              self.channel_name
          )
          await self.accept()


    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['user']
        await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat.message',
                        'message': message,
                        'username': username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )