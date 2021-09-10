from rest_framework import serializers
from .models import Movie, Rating

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

class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("star", "movie")

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get("ip", None),
            movie=validated_data.get("movie", None),
            defaults={"star": validated_data.get("star")}
        )
        return rating