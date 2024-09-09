from django.contrib import admin
from .models import User, Card, List, Board, EpicLink


admin.site.register(User)
admin.site.register(Card)
admin.site.register(List)
admin.site.register(Board)
admin.site.register(EpicLink)
