from django.urls import path, include
from django.contrib.auth import views 
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
    path('', views.new_game_session, name='new_game_session'),
    path('game/<int:game_session_id>/', views.join_game_session, name='game_lobby'),
    path('game/<int:game_session_id>/characters/', views.display_characters, name='display_characters'),
    path('game/<int:game_session_id>/guess/', views.handle_guess, name='handle_guess'),
    path('game/<str:game_session_id>/', include('game.routing')),
]
