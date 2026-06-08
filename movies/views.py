from django.shortcuts import render, get_object_or_404
from .models import Movie
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MovieSerializer, DetailSerializer


class MoviePagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 50


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.filter(is_published=True)
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'director', 'cast']
    ordering_fields = ['year', 'rating', 'id']
    ordering = ['-id']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailSerializer
        return MovieSerializer


def movie_list(request):
    movies = Movie.objects.filter(is_published=True)
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug, is_published=True)
    return render(request, 'movies/movie_detail.html', {'movie': movie})