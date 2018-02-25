from djangorestframework_camel_case.util import underscoreize
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import (
    Ability,
    Character,
    Game,
    Item,
)
from .mocks import (
    create_game_mock,
    create_character_mock,
    create_item_mock,
    create_ability_mock,
)


class CharacterTestCase(TestCase):
    """Test suite for the character endpoints."""

    def _post(self, data):
        return self.client.post(
            reverse('character'),
            data,
            format="json"
        )

    def _put(self, id, data):
        return self.client.put(
            reverse('character/pk', args=[id]),
            data,
            format="json"
        )

    def _patch(self, id, data):
        return self.client.patch(
            reverse('character/pk', args=[id]),
            data,
            format="json"
        )

    def _delete(self, id):
        return self.client.delete(
            reverse('character/pk', args=[id]),
            format="json"
        )

    def _get(self):
        return self.client.get(
            reverse('character'),
            format="json"
        )

    def setUp(self):
        """Define the test client."""
        self.client = APIClient()

    def _assert_character_props(self, character, data):
        self.assertEqual(character.age, data.get('age'))
        self.assertEqual(character.name, data.get('name'))
        self.assertEqual(character.race, data.get('race'))
        self.assertEqual(character.level, data.get('level'))
        self.assertEqual(character.game.id, data.get('game'))
        self.assertEqual(character.player, data.get('player'))
        self.assertEqual(character.class_name, data.get('class_name'))
        self.assertEqual(character.magic_points, data.get('magic_points'))
        self.assertEqual(character.health_points, data.get('health_points'))
        self.assertEqual(character.items.count(), data.get('items').__len__())
        self.assertEqual(character.abilities.count(), data.get('abilities').__len__())

    def _assert_created_character_nested_props(self, character, data):
        ability = character.abilities.first()
        self.assertEqual(ability.name, data.get('abilities')[0]['name'])
        self.assertEqual(ability.description, data.get('abilities')[0]['description'])
        item = character.items.first()
        self.assertEqual(item.name, data.get('items')[0]['name'])
        self.assertEqual(item.description, data.get('items')[0]['description'])

    def _test_post(self, assertions_cb, **kwargs):
        count = kwargs.pop('count', 0)
        self.assertEqual(Character.objects.count(), count)

        data = create_character_mock(
            game=kwargs.pop('game'),
            items=[create_item_mock()],
            abilities=[create_ability_mock()],
            **kwargs
        )
        response = self._post(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Character.objects.count(), count + 1)
        character = Character.objects.last()
        assertions_cb(character, data)

    def test_post(self):
        """Test POST request to 'character' api'"""
        def assertions_cb(character, data):
            self._assert_character_props(character, data)
            self._assert_created_character_nested_props(character, data)

        game = Game.objects.create(**create_game_mock())
        self._test_post(assertions_cb, game=game.id)

    def _test_put(self, id, assertions_cb, **kwargs):
        self.assertEqual(Character.objects.count(), 1)

        data = create_character_mock(**kwargs)
        data['id'] = id

        response = self._put(id, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Character.objects.count(), 1)
        character = Character.objects.first()
        assertions_cb(character)

    def test_put(self):
        """Test PUT request to 'character' api'"""
        def assertions_cb(character, data):
            self._assert_character_props(character, data)
            self._assert_created_character_nested_props(character, data)

        game = Game.objects.create(**create_game_mock())
        self._test_post(assertions_cb, game=game.id)

        saved_character = Character.objects.first()
        game = Game.objects.create(**create_game_mock(
            name="Pathfinder",
            sumary="Community D&D 3.5 compatible system",
        ))
        rage = saved_character.abilities.first()
        new_data = {
            'name': 'Durotan',
            'player': 'CPU',
            'race': 'Orc',
            'game': game.id,
            'age': 35,
            'class_name': 'Barbarian',
            'level': 15,
            'health_points': 200,
            'magic_points': 0,
            'items': [{
                'name': 'Great Axe',
                'description': 'Double edge war axe',
            }],
            'abilities': [{
                'id': rage.id,
                'name': 'Rage',
                'description': 'Goes berserker. Get stronger and crazier',
            }, {
                'name': 'Power Attack',
                'description': 'Focus on damage sacrificing precision',
            }],
        }

        def updated_assertions_cb(character):
            self._assert_character_props(character, new_data)

            rage_ability = character.abilities.get(id=rage.id)
            self.assertEqual(rage_ability.name, new_data.get('abilities')[0]['name'])
            self.assertEqual(rage_ability.description, new_data.get('abilities')[0]['description'])
            power_attak_ability = character.abilities.exclude(id=rage.id).first()
            self.assertEqual(power_attak_ability.name, new_data.get('abilities')[1]['name'])
            self.assertEqual(power_attak_ability.description, new_data.get('abilities')[1]['description'])
            item = character.items.first()
            self.assertEqual(item.name, new_data.get('items')[0]['name'])
            self.assertEqual(item.description, new_data.get('items')[0]['description'])

        self._test_put(saved_character.id, updated_assertions_cb, **new_data)

    def _test_patch(self, id, assertions_cb, **kwargs):
        self.assertEqual(Character.objects.count(), 1)

        data = {**kwargs}
        data['id'] = id

        response = self._patch(id, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Character.objects.count(), 1)
        character = Character.objects.first()
        assertions_cb(character)

    def test_patch(self):
        """Test PATCH request to 'character' api'"""
        def assertions_cb(character, data):
            self._assert_character_props(character, data)
            self._assert_created_character_nested_props(character, data)

        game = Game.objects.create(**create_game_mock())
        self._test_post(assertions_cb, game=game.id)

        saved_character = Character.objects.first()
        new_data = {
            'name': 'Durotan',
            'magic_points': 0,
        }

        def updated_assertions_cb(character):
            self.assertEqual(character.name, 'Durotan')
            self.assertEqual(character.magic_points, 0)

        self._test_patch(saved_character.id, updated_assertions_cb, **new_data)

    def _test_delete(self, id, assertions_cb):
        self.assertEqual(Character.objects.count(), 1)

        response = self._delete(id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Character.objects.count(), 0)
        assertions_cb()

    def test_delete(self):
        """Test DELETE request to 'character' api'"""
        def assertions_cb(character, data):
            self._assert_character_props(character, data)
            self._assert_created_character_nested_props(character, data)

        game = Game.objects.create(**create_game_mock())
        self._test_post(assertions_cb, game=game.id)
        saved_character = Character.objects.first()

        def deleted_assertions_cb():
            self.assertFalse(Character.objects.exists())

        self._test_delete(saved_character.id, deleted_assertions_cb)

    def test_get(self):
        """Test GET request to 'character' api'"""
        game1 = Game.objects.create(**create_game_mock(name='Game 1'))
        game2 = Game.objects.create(**create_game_mock(name='Game 2'))
        games = [game1, game2]
        for count in range(0, 4):
            def assertions_cb(character, data):
                self._assert_character_props(character, data)
                self._assert_created_character_nested_props(character, data)

            self._test_post(
                assertions_cb,
                name='test_' + str(count),
                count=count,
                game= games[count % 2].id,
            )

        grouped_collection = underscoreize(self._get().data)
        self.assertEqual(grouped_collection[0]['game_name'], 'Game 1')
        self.assertEqual(grouped_collection[0]['game_id'], game1.id)
        self.assertEqual(grouped_collection[0]['characters'][0]['name'], 'test_0')
        self.assertEqual(grouped_collection[0]['characters'][1]['name'], 'test_2')

        self.assertEqual(grouped_collection[1]['game_name'], 'Game 2')
        self.assertEqual(grouped_collection[1]['game_id'], game2.id)
        self.assertEqual(grouped_collection[1]['characters'][0]['name'], 'test_1')
        self.assertEqual(grouped_collection[1]['characters'][1]['name'], 'test_3')

