
from django.db import models
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import CreateRatingSerializer, MovieListSerializer, MovieDetailSerializer

from .service import get_client_ip, MovieFilter

# Create your views here.


class MovieListView(generics.ListAPIView):
    serializer_class = MovieListSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = MovieFilter

    def get_queryset(self):
        movies = Movie.objects.all().annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F("ratings__star")) / models.Count(models.F("ratings"))
        ).annotate(
            rating_count=models.Count("ratings")
        )
        return movies


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.filter()
    serializer_class = MovieDetailSerializer


class AddStarRatingView(generics.CreateAPIView):
    serializer_class = CreateRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class LogOut(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=200)