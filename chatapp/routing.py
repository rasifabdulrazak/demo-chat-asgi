from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path,path
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/', ChatConsumer.as_asgi()),
]