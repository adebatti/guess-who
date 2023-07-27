# game/routing.py

from django.urls import path
from .consumers import GameConsumer

websocket_urlpatterns = [
    path('ws/game/<int:game_session_id>/', GameConsumer.as_asgi()),
]
