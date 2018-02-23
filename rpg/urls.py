from django.conf.urls import url
from .views import (
    CharacterList,
    CharacterDetail,
    GameList,
    GameDetail,
)

urlpatterns = [
    url(r'^character/$', CharacterList.as_view(), name="character"),
    url(r'^character/(?P<pk>[0-9]+)/$', CharacterDetail.as_view(), name="character/pk"),
    url(r'^game/$', GameList.as_view(), name="game"),
    url(r'^game/(?P<pk>[0-9]+)/$', GameDetail.as_view(), name="game/pk"),
]

