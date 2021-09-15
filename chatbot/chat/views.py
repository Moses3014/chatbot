from django.shortcuts import render
# from urllib import request,response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from .serialize import ChatMsgSerializer,ChatSerializer
from .models import Chat,ChatMsg
from django.db.models import Q
from django.db import connection
import json

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all().order_by('id')
    serializer_class = ChatSerializer

class ChatMsgViewSet(viewsets.ModelViewSet):
    queryset = ChatMsg.objects.all().order_by('id')
    serializer_class = ChatMsgSerializer



@api_view(['GET','POST'])
def getChat(request):
    try:
        sender_id = request.data["sender_id"]
        requisition_id = request.data["requisition_id"]

        chats = Chat.objects.filter((Q(sender_id__exact=sender_id) | Q(receiver_id__exact = sender_id)) & Q(requisition_id__exact=requisition_id))
        chatserialize = ChatSerializer(chats,many=True)
        data = dict({
            "status":"success",
            "results":chatserialize.data
            })
        return Response(data)
    except:
        data = dict({
            "status":"failed",
        })
        return Response(data)


@api_view(['GET','POST'])
def setChat(request):
    try:
        msg = request.data["msg"]
        sender_id = request.data["sender_id"]
        receiver_id = request.data["receiver_id"]
        requisition_id = request.data["requisition_id"]
        nc = Chat(msg=msg,sender_id=sender_id,receiver_id=receiver_id,requisition_id=requisition_id)
        # return Response("Hello World")
        
        nc.save()
        data = dict({"status":"success"})
        return Response(data)
    except:
        data = dict({"status":"failed"})
        return Response(data)
# Create your views here.

@api_view(['GET'])
def index(request):
    return Response("Hello World")

