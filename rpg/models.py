from django.db import models

class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    sumary = models.TextField()

    def __str__(self):
        return name

    class Meta:
        ordering = ('created_at',)

class Character(models.Model):
    age = models.IntegerField()
    class_name = models.CharField(max_length=100)
    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE,
    )
    health_points = models.IntegerField()
    level = models.IntegerField()
    magic_points = models.IntegerField()
    name = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    race = models.CharField(max_length=100)

    def __str__(self):
        return u"{} , {} - LV: {}".format(
            self.name,
            self.class_name,
            self.level
        )

    class Meta:
        ordering = ('name',)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE
    )

class Ability(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE
    )

