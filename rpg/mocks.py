from datetime import datetime

def create_game_mock(
        name="Dungeons & Dragons",
        sumary="Medieval fantasy adventures on D20 based systems",
    ):
    return {
        'name': name,
        'sumary': sumary,
    }

def create_item_mock(
        name="Vorpal Sword",
        description="Pierces anything",
    ):
    return {
        'name': name,
        'description': description,
    }

def create_ability_mock(
        name="Sneak Attack",
        description="deals extra damage when you catch the enemy off guard",
    ):
    return {
        'name': name,
        'description': description,
    }

def create_character_mock(
        game=1,
        name="Melkor",
        player="Vin Diesel",
        age=20,
        race="Human",
        class_name="Witch Hunter",
        level=20,
        health_points=300,
        magic_points=150,
        items=[],
        abilities=[],
    ):
    return {
        'name': name,
        'player': player,
        'race': race,
        'game': game,
        'age': age,
        'class_name': class_name,
        'level': level,
        'health_points': health_points,
        'magic_points': magic_points,
        'items': items,
        'abilities': abilities,
    }

