from django.conf.urls import url
from .views import (
    AbilityList,
    AbilityDetail,
    CharacterList,
    CharacterDetail,
    GameList,
    GameDetail,
    ItemList,
    ItemDetail,
)

urlpatterns = [
    url(r'^ability/$', AbilityList.as_view(), name="ability"),
    url(r'^ability/(?P<pk>[0-9]+)/$', AbilityDetail.as_view(), name="ability/pk"),
    url(r'^character/$', CharacterList.as_view(), name="character"),
    url(r'^character/(?P<pk>[0-9]+)/$', CharacterDetail.as_view(), name="character/pk"),
    url(r'^game/$', GameList.as_view(), name="game"),
    url(r'^game/(?P<pk>[0-9]+)/$', GameDetail.as_view(), name="game/pk"),
    url(r'^item/$', ItemList.as_view(), name="item"),
    url(r'^item/(?P<pk>[0-9]+)/$', ItemDetail.as_view(), name="item/pk"),
]

