from django.contrib import admin
from .models import Chat
from .models import ChatMsg

# Register your models here.

admin.site.register(Chat)
admin.site.register(ChatMsg)