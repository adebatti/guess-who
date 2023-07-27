# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from game.consumers import GameConsumer

websocket_urlpatterns = [
    path('ws/game/<str:game_session_id>/', GameConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
