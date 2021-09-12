
from django.db import models
from rest_framework import generics

from .models import Movie
from .serializers import CreateRatingSerializer, MovieListSerializer, MovieDetailSerializer
from .service import get_client_ip

# Create your views here.


class MovieListView(generics.ListAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        movies = Movie.objects.all().annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F("ratings__star")) / models.Count(models.F("ratings"))
        )
        return movies


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.filter()
    serializer_class = MovieDetailSerializer


class AddStarRatingView(generics.CreateAPIView):
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))