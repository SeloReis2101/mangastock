import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message
from authentication.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f"chat_{self.chat_id}"

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'add_message':
            await self.channel_layer.group_send(
                self.chat_group_name,
                {
                    'type': 'send_message_add',
                    'data': data,
                }
            )
        elif action == 'edit_message':
            message_id = data["message"]['id']
            new_message = data["message"]["new_content"]
            await self.edit_message(message_id, new_message)
            await self.channel_layer.group_send(
                self.chat_group_name,
                {
                    'type': 'send_message_edit',
                    'data': data,
                }
            )
        elif action == 'delete_message':
            message_id = data["message"]['id']
            await self.delete_message(message_id)
            await self.channel_layer.group_send(
                self.chat_group_name,
                {
                    'type': 'send_message_delete',
                    'data': data
                }
            )

    async def send_message_add(self, event):
        data = event["data"]
        data["action"] = 'message_added'
        message = await self.add_message(event["data"])
        data["message"]["id"] = message.id
        await self.send(text_data=json.dumps(data))

    async def send_message_edit(self, event):
        data = event["data"]
        data["action"] = 'message_edited'
        await self.send(text_data=json.dumps(data))

    async def send_message_delete(self, event):
        data = event["data"]
        data["action"] = 'message_deleted'
        await self.send(text_data=json.dumps(data))


    # sync_to_async helper functions
    @sync_to_async
    def add_message(self, data):
        message = Message.objects.create(chat_id=self.chat_id, sender=User.objects.get(username=data["user"]["username"]), content=data["message"]["content"])
        message.save()
        return message

    @sync_to_async    
    def delete_message(self, message_id):
        Message.objects.get(id=message_id).delete()

    @sync_to_async 
    def edit_message(self, message_id, new_message):
        message = Message.objects.get(id=message_id)
        message.content = new_message
        message.save()