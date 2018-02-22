from rest_framework import serializers
from .models import (
    Ability,
    Character,
    Game,
    Item,
)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'description')

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ('id', 'name', 'description')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'sumary', 'created_at')

class CharacterSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    abilities = AbilitySerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = (
            'id',
            'game',
            'name',
            'player',
            'age',
            'race',
            'level',
            'class',
            'health_points',
            'magic_points',
            'items',
            'abilities',
        )

CharacterSerializer._declared_fields["class"] = serializers.CharField(source="class_name")

