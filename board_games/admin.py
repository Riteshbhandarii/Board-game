from django.contrib import admin
from .models import BoardGame, BorrowedGame

admin.site.register(BoardGame)
admin.site.register(BorrowedGame)
