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
    items = ItemSerializer(many=True)
    abilities = AbilitySerializer(many=True)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        abilities_data = validated_data.pop('abilities')
        character = Character.objects.create(**validated_data)

        for item_data in items_data:
            Item.objects.create(character=character, **item_data)

        for ability_data in abilities_data:
            Ability.objects.create(character=character, **ability_data)

        return character

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        abilities_data = validated_data.pop('abilities')

        for k, v in validated_data.items():
            setattr(instance, k, v if v else getattr(instance, k))

        instance.save()
        return instance

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

