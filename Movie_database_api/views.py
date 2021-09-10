
from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import CreateRatingSerializer, MovieListSerializer, MovieDetailSerializer
from .service import get_client_ip

# Create your views here.

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all().annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(request)))
        ).annotate(
            middle_star=models.Sum(models.F("ratings__star")) / models.Count(models.F("ratings"))
        )
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

class AddStarRatingView(APIView):
    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)