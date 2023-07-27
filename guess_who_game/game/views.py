# views.py
import random
from django.shortcuts import render, redirect
from .models import Character, Player, GameSession
from .game_logic import set_active_character, is_game_active

# Function to generate random characters for a game session
def generate_random_characters(game_session, num_characters=24):
    all_characters = list(Character.objects.all())
    random.shuffle(all_characters)
    selected_characters = all_characters[:num_characters]
    game_session.characters.set(selected_characters)

def new_game_session(request):
    # Create a new game session with default settings
    game_session = GameSession.objects.create(is_active=True)

    # Generate random characters for the game session
    generate_random_characters(game_session)

    # Set the active character for the game session
    set_active_character(game_session)

    # Redirect to the game lobby with the newly created game_session_id
    return redirect('game_lobby', game_session_id=game_session.id)

# Function to handle player guesses
def handle_guess(request, game_session_id):
    if request.method == 'POST':
        try:
            game_session = GameSession.objects.get(id=game_session_id)
        except GameSession.DoesNotExist:
            return render(request, 'game/join_session_error.html')

        if not game_session.is_active:
            return render(request, 'game/join_session_error.html')

        character_id = request.POST.get('character_id')
        try:
            guessed_character = Character.objects.get(id=character_id)
        except Character.DoesNotExist:
            return render(request, 'game/guess_error.html')

        if guessed_character == game_session.active_character:
            game_session.is_active = False
            game_session.save()
            return render(request, 'game/correct_guess.html', {'guessed_character': guessed_character})
        else:
            return render(request, 'game/incorrect_guess.html', {'guessed_character': guessed_character})

    return redirect('game_lobby', game_session_id=game_session_id)

def join_game_session(request, game_session_id):
    try:
        game_session = GameSession.objects.get(id=game_session_id)
    except GameSession.DoesNotExist:
        # Handle if the game session does not exist
        return render(request, 'game/join_session_error.html')

    if not game_session.is_active:
        # Handle if the game session is already completed
        return render(request, 'game/join_session_error.html')

    return render(request, 'game/game_lobby.html', {'game_session': game_session})

def display_characters(request, game_session_id):
    try:
        game_session = GameSession.objects.get(id=game_session_id)
    except GameSession.DoesNotExist:
        # Handle if the game session does not exist
        return render(request, 'game/join_session_error.html')

    characters = game_session.characters.all()

    return render(request, 'game/display_characters.html', {'characters': characters, 'game_session_id': game_session_id})

""" def handle_guess(request, game_session_id):
    if request.method == 'POST':
        try:
            game_session = GameSession.objects.get(id=game_session_id)
        except GameSession.DoesNotExist:
            # Handle if the game session does not exist
            return render(request, 'game/join_session_error.html')

        if not game_session.is_active:
            # Handle if the game session is already completed
            return render(request, 'game/join_session_error.html')

        character_id = request.POST.get('character_id')
        try:
            guessed_character = Character.objects.get(id=character_id)
        except Character.DoesNotExist:
            # Handle if the guessed character does not exist
            return render(request, 'game/guess_error.html')

        if guessed_character == game_session.active_character:
            # Correct guess, mark the game session as completed
            game_session.is_active = False
            game_session.save()
            return render(request, 'game/correct_guess.html', {'guessed_character': guessed_character})
        else:
            # Incorrect guess, continue the game
            return render(request, 'game/incorrect_guess.html', {'guessed_character': guessed_character})

    return redirect('game_lobby', game_session_id=game_session_id) """
