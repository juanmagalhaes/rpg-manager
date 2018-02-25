from djangorestframework_camel_case.util import camelize
from rest_framework import serializers
from django.db import transaction
from .models import (
    Ability,
    Character,
    Game,
    Item,
)

def map_to_related_model(character, Entity, data):
    return list(map(lambda x:
        Entity(character=character, **x), data))

class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Item
        fields = ('id', 'name', 'description')

class AbilitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Ability
        fields = ('id', 'name', 'description')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'sumary', 'created_at')

class CharacterListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        def mapper(game):
            return {
                'characters': camelize([*data.filter(game=game).values()]),
                'game_name': game.name,
                'game_id': game.id,
            }
        return list(map(mapper, Game.objects.all()))


class CharacterSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, required=False)
    abilities = AbilitySerializer(many=True, required=False)

    class Meta:
        model = Character
        list_serializer_class = CharacterListSerializer
        fields = ('__all__')

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        abilities_data = validated_data.pop('abilities', [])
        character = Character.objects.create(**validated_data)
        character.items.bulk_create(map_to_related_model(
            character,
            Item,
            items_data
        ))
        character.abilities.bulk_create(map_to_related_model(
            character,
            Ability,
            abilities_data
        ))
        return character

    @transaction.atomic
    def update(self, instance, validated_data):
        def create_new_nested_models(nested_set, collection):
            new_nested_models = list(filter(lambda x: not x.id, collection))
            nested_set.bulk_create(new_nested_models)

        def update_existing_nested_models(nested_set, collection):
            existing_nested_models = list(filter(lambda x: x.id, collection))
            for item in existing_nested_models:
                item.save()
                nested_set.add(item)

        def delete_old_nested_models(nested_set, collection):
            old_nested_models = list(map(lambda x: x.id, collection))
            nested_set.exclude(id__in=old_nested_models).delete()

        items_data = validated_data.pop('items', [])
        item_collection = map_to_related_model(
            instance,
            Item,
            items_data
        )
        create_new_nested_models(instance.items, item_collection)
        update_existing_nested_models(instance.items, item_collection)
        delete_old_nested_models(instance.items, item_collection)

        abilities = validated_data.pop('abilities', [])
        ability_collection = map_to_related_model(
            instance,
            Ability,
            abilities
        )
        create_new_nested_models(instance.abilities, ability_collection)
        update_existing_nested_models(instance.abilities, ability_collection)
        delete_old_nested_models(instance.abilities, ability_collection)

        for k, v in validated_data.items():
            setattr(instance, k, v)

        instance.save()
        return instance

