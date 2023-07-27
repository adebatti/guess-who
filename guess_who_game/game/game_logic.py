# game/game_logic.py

import random
from .models import Character

# Function to get a random character from the available characters in a game session
def get_random_character(game_session):
    characters = game_session.characters.all()
    return random.choice(characters)

# Function to set the active character for a game session
def set_active_character(game_session):
    game_session.active_character = get_random_character(game_session)
    game_session.save()

# Function to check if the game session is active
def is_game_active(game_session_id):
    try:
        game_session = GameSession.objects.get(id=game_session_id)
        return game_session.is_active
    except GameSession.DoesNotExist:
        return False
