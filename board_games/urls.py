# board_games/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # User Authentication
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # Profile and Borrowing Games
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("borrow_game/<int:game_id>/", views.borrow_game, name="borrow_game"),
    path("return_game/<int:game_id>/", views.return_game, name="return_game"),
]
