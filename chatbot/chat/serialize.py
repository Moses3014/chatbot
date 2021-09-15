from rest_framework import serializers

from .models import Chat,ChatMsg

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        # fields = ('id', 'sender_id','receiver_id','msg')
        fields = '__all__'

class ChatMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMsg
        # fields = ('id', 'chat_msg','symbol')
        fields = '__all__'
