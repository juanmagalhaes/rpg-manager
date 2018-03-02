from django.db import models
from django.utils.timezone import now

class Game(models.Model):
    name = models.CharField(max_length=100)
    sumary = models.TextField()
    created_at = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)

class Character(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='characters'
    )
    name = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    age = models.IntegerField()
    avatar = models.URLField(blank=True, default='', max_length=400)
    race = models.CharField(max_length=100)
    character_class = models.CharField(max_length=100)
    level = models.IntegerField()
    health_points = models.IntegerField()
    magic_points = models.IntegerField()

    def __str__(self):
        return u"{} , {} - LV: {}".format(
            self.name,
            self.character_class,
            self.level
        )

    class Meta:
        ordering = ('name',)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='items'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Ability(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='abilities'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

