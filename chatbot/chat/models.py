from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# declare a new model with a name "Chat"
class Chat(models.Model):
    msg = models.CharField(max_length=100)
    sender_id = models.IntegerField(unique=False)
    receiver_id = models.IntegerField(unique=False)
    requisition_id = models.IntegerField(unique=False)
    status = models.TextField(max_length=10,default="A")
    # content = models.TextField()
    # date_chated = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
#renames the instances of the model with their msg name
    def __str__(self):  
        return self.msg

    class Meta:
        db_table = "chat"


class ChatMsg(models.Model):
    chat_msg = models.TextField(max_length=100)
    symbol = models.TextField(max_length=100)
    status = models.TextField(max_length=10)
    def __str__(self):
        return self.chat_msg
    
    class Meta:
        db_table = "chat_msg"