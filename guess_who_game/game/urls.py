from django.urls import path
from . import views

urlpatterns = [
    # URL pattern to start a new game session
    path('game/new/', views.new_game_session, name='new_game_session'),

    # URL pattern to join an existing game session
    path('game/join/<int:game_session_id>/', views.join_game_session, name='join_game_session'),

    # URL pattern to display characters to players for guessing
    path('game/display/<int:game_session_id>/', views.display_characters, name='display_characters'),

    # URL pattern to handle player guesses
    path('game/guess/<int:game_session_id>/', views.handle_guess, name='handle_guess'),
]
