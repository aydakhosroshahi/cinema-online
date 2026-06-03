from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_list(request):
    movies = Movie.objects.filter(is_published=True)
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug, is_published=True)
    return render(request, 'movies/movie_detail.html', {'movie': movie})