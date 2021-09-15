from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("movies/", views.MovieListView.as_view()),
    path("movie/<int:pk>/", views.MovieDetailView.as_view()),
    path("rating/", views.AddStarRatingView.as_view()),

    path("auth/", include("djoser.urls")),
    path("auth/token", obtain_auth_token, name="token"),
]