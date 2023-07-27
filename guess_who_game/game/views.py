# views.py

from django.shortcuts import render, redirect
from .models import Character, Player, GameSession

def new_game_session(request):
    # Create a new game session with default settings
    game_session = GameSession.objects.create(is_active=True)

    # Redirect to the game lobby with the newly created game_session_id
    return redirect('game_lobby', game_session_id=game_session.id)

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

def handle_guess(request, game_session_id):
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

    return redirect('game_lobby', game_session_id=game_session_id)
