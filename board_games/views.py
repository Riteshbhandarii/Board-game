# board_games/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BoardGame, BorrowedGame


# Sign up a new user
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(
                request, user
            )  # Automatically log in the user after successful sign-up
            messages.success(request, "Account created successfully!")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = UserCreationForm()
    return render(request, "board_games/signup.html", {"form": form})


# Log in an existing user
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "board_games/login.html")


# Log out the user
def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout


# View the user's profile and borrowed games
@login_required
def profile(request):
    borrowed_games = BorrowedGame.objects.filter(user=request.user)
    return render(
        request, "board_games/profile.html", {"borrowed_games": borrowed_games}
    )


# Edit user's profile (if needed, add more fields to User model)
@login_required
def edit_profile(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")
    return render(request, "board_games/edit_profile.html")


# Borrow a game (ensuring they don't borrow more than 3 games)
@login_required
def borrow_game(request, game_id):
    game = BoardGame.objects.get(id=game_id)

    # Check if user already has 3 borrowed games
    if BorrowedGame.objects.filter(user=request.user).count() >= 3:
        messages.error(request, "You can't borrow more than 3 games at a time.")
        return redirect("profile")

    # Create a record in BorrowedGame model
    borrowed_game = BorrowedGame(user=request.user, game=game)
    borrowed_game.save()
    messages.success(request, f"You've successfully borrowed {game.name}.")
    return redirect("profile")


# Return a borrowed game
@login_required
def return_game(request, game_id):
    borrowed_game = BorrowedGame.objects.get(id=game_id, user=request.user)
    borrowed_game.delete()
    messages.success(request, "You've successfully returned the game.")
    return redirect("profile")
