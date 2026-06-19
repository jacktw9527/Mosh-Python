from django.http import HttpRequest, HttpResponse, Http404
from .models import Movie
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """View function for home page of site."""
    movies = Movie.objects.all()  # type: ignore
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request: HttpRequest, movie_id: int) -> HttpResponse:
    """View function for detail page of site."""
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
