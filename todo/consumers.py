import json
from .models import MyUser
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
 # that page handle server movement with handlers what the server will response.


class mywebsocket(WebsocketConsumer):
      def connect(self): # handler for request for connection to server
          print('connect')
          print('channel layer',self.channel_layer)
          print('channel name ',self.channel_name)
          receiver = self.scope['url_route']['kwargs']['user_name']
          print(receiver)


          self.accept()# connection accept handler by server
        
      def receive(self, text_data=None, bytes_data=None):# handler for message receive from server
           # print('message recive from client',text_data)
            payload = json.loads(text_data)
            print(payload['user'])
            print(payload['receiver'])

            from_user =async_to_sync(MyUser.objects.get(name=payload['user']))
            print(from_user)    # get user object of friend
            to_user =async_to_sync(MyUser.objects.get)(name=payload['receiver'])

            # text_data_json = json.loads(text_data)# messsage receive in string so we can't use python function on this most of.
            # json.loads change string data into python __dict__ data type for making it  a key value pair
            message = payload['message'] # get message from client and assgin into message with the help of __dict__ key message now value will assign
           
            self.send(text_data=json.dumps({ # send the response to client after change the data __dict__ to string with the help of json.dumps
                'message' : message
            }))

      def disconnect(self, code):
            return super().disconnect(code)
