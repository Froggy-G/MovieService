from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Actor(models.Model):
    name = CharField(verbose_name="Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):
    name = CharField(verbose_name="Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    title = CharField(verbose_name="Название", max_length=100)
    directors = ManyToManyField(
        Actor, verbose_name="Режиссер", related_name="film_director"
    )
    actors = ManyToManyField(Actor, verbose_name="Актеры", related_name="film_actor")
    genre = ManyToManyField(Genre, verbose_name="Жанры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Rating(models.Model):
    user_id = CharField(verbose_name="Id пользователя", max_length=15, default=None)
    star = IntegerField(verbose_name="Звезда", validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = ForeignKey(
        Movie, on_delete=CASCADE, verbose_name="Фильм", related_name="ratings"
    )

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
