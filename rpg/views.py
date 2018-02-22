from .serializers import (
    AbilitySerializer,
    CharacterSerializer,
    GameSerializer,
    ItemSerializer,
)
from .models import (
    Ability,
    Character,
    Game,
    Item,
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

class AbilityList(ListCreateAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

class AbilityDetail(RetrieveUpdateDestroyAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer

class CharacterList(ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class GameList(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class ItemList(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

