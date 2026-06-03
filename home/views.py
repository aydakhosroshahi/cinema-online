from django.shortcuts import render
from movies.models import Movie, Genre


def index(request):
    latest_movies = Movie.objects.filter(is_published=True).order_by('-id')
    slider_movies = Movie.objects.filter(is_published=True).order_by('-id')[:5]  

    years = Movie.objects.filter(is_published=True).values_list('year', flat=True).distinct().order_by('-year')
    genres = Genre.objects.all()

    categories = [
        {'name': 'اکشن', 'image': 'action.png', 'count': '120'},
        {'name': 'عاشقانه', 'image': 'romantic.png', 'count': '85'},
        {'name': 'کمدی', 'image': 'comedy.png', 'count': '95'},
        {'name': 'درام', 'image': 'drama.png', 'count': '110'},
        {'name': 'ترسناک', 'image': 'scary.png', 'count': '65'},
        {'name': 'علمی-تخیلی', 'image': 'science-fiction.png', 'count': '78'},
        {'name': 'ماجراجویی', 'image': 'adv.png', 'count': '92'},
        {'name': 'انیمیشن', 'image': 'animation.png', 'count': '70'},
    ]

    context = {
        'latest_movies': latest_movies,
        'slider_movies': slider_movies,
        'years': years,
        'genres': genres,
        'categories': categories,
    }
    return render(request, 'home/index.html', context)