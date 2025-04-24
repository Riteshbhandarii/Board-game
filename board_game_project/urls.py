# board_game_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # Django admin page
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # Auth-related URLs (login/logout)
    path(
        "board_games/", include("board_games.urls")
    ),  # Include URLs from board_games app
]
