from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", )

class MovieDetailSerializer(serializers.ModelSerializer):
    directors = serializers.SlugRelatedField(slug_field="name", read_only='True', many='True')
    actors = serializers.SlugRelatedField(slug_field="name", read_only='True', many='True')
    genre = serializers.SlugRelatedField(slug_field="name", read_only='True', many='True')

    class Meta:
        model = Movie
        fields = "__all__"