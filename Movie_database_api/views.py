from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer

# Create your views here.

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

