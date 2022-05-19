# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/todo/(?P<user_name>\w+)/$', consumers.mywebsocket.as_asgi()),
]