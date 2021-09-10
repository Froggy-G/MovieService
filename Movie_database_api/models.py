from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, PositiveSmallIntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.

class Actor(models.Model):
    name = CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"

class Genre(models.Model):
    name = CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    title = CharField("Название", max_length=100)
    directors = ManyToManyField(Actor, verbose_name = "Режиссер", related_name="film_director")
    actors = ManyToManyField(Actor, verbose_name = "Актеры", related_name="film_actor")
    genre = ManyToManyField(Genre, verbose_name = "Жанры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class RatingStar(models.Model):
    value = PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"

class Rating(models.Model):
    ip = CharField("IP адрес", max_length=15)
    star = ForeignKey(RatingStar, on_delete=CASCADE, verbose_name="Звезда")
    movie = ForeignKey(Movie, on_delete=CASCADE, verbose_name="Фильм", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"    