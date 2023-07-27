
# models.py

from django.db import models

# Define the Character model to represent characters in the game
class Character(models.Model):
    name = models.CharField(max_length=100)        # Name of the character
    image_url = models.URLField()                 # URL of the character's image
    description = models.TextField()              # Description of the character (optional)

    def __str__(self):
        return self.name

# Define the Player model to represent players participating in the game
class Player(models.Model):
    name = models.CharField(max_length=100)        # Name of the player
    avatar_url = models.URLField(default="https://example.com/default-avatar.png")  # URL of the player's avatar image (default provided)

    def __str__(self):
        return self.name

# Define the GameSession model to represent a session where players play the Guess Who game
class GameSession(models.Model):
    access_code = models.CharField(max_length=8, unique=True)   # Unique access code for each game session
    players = models.ManyToManyField(Player)                    # Players participating in the game session (many-to-many relationship)
    characters = models.ManyToManyField(Character)              # Characters available for selection in the game (many-to-many relationship)
    active_character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True, blank=True)  # Currently selected character for guessing
    is_active = models.BooleanField(default=True)               # Flag to indicate if the game session is active or completed

    def __str__(self):
        return f"Game Session #{self.id}"
