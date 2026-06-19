from ninja import Router
from .models import Movie
from .schemas import MovieSchema
from django.shortcuts import get_object_or_404

router = Router(tags=['movies'])

@router.get('/movies', response=list[MovieSchema])
def get_movies(request):
    return Movie.objects.select_related('genre').all()

@router.get('/movies/{movie_id}', response=MovieSchema)
def get_movie(request, movie_id: int):
    return get_object_or_404(
      Movie.objects.select_related('genre'),  # type: ignore
      id=movie_id)
