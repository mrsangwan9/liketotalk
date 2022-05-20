# chat/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/todo/<int:other_id>/', consumers.myasyncconsumer.as_asgi()),
]