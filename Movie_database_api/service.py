from django_filters import rest_framework as filters
from .models import Movie


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MovieFilter(filters.FilterSet):
    actors = CharFilterInFilter(field_name="actors__name", lookup_expr="in")
    directors = CharFilterInFilter(field_name="directors__name", lookup_expr="in")

    class Meta:
        model = Movie
        fields = ["actors", "directors"]
