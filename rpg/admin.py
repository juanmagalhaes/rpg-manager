from django.contrib import admin
from .models import (
    Ability,
    Character,
    Game,
    Item
)

admin.site.register(Ability)
admin.site.register(Character)
admin.site.register(Game)
admin.site.register(Item)
