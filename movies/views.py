from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Score, Genre
from django.db.models import Avg
from .forms import MovieForm

# Create your views here.
def index(request):
    # a = Movie.objects.filter(title='title')
    # movies = Movie.objects.all()
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    # print(movies_genre)
    return render(request, 'index.html',{'movies': movies})
    
def new(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect(movie)
    else:
        movie_form = MovieForm()
    context = {'movie_form': movie_form}
    return render(request, 'form.html', context)

def edit(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie = movie_form.save()
            return redirect(movie)
    else:
        movie_form = MovieForm(instance=movie)
    context = {'movie_form': movie_form}
    return render(request, 'form.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    scores = movie.score_set.all
    context = {
        'movie':movie,
        'scores':scores
    }
    return render(request, 'detail.html', context)
    
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')

def scnew(request, movie_pk):
    if request.method == "POST":
        movie = Movie.objects.get(pk=movie_pk)
        score = Score()
        score.content = request.POST.get('content')
        score.score =  request.POST.get('score')
        score.movie = movie
        # score = Score(content=content, score=score)
        score.save()
    return redirect('movies:detail', movie_pk)
    
def scdel(request, movie_pk, score_pk):
    if request.method == "POST":
        score = Score.objects.get(pk=score_pk)
        score.delete()
    return redirect('movies:detail', movie_pk)
    # movie.pk 가 아닌 movie_pk 를 넘겨줘야함.
    
    
    

    
def update(request, pk):
    u_movie = Movie.objects.get(pk=pk)
    u_movie.title = request.POST.get('title')
    u_movie.audience = request.POST.get('audience')
    u_movie.genre = request.POST.get('genre')
    u_movie.score = request.POST.get('score')
    u_movie.poster_url = request.POST.get('poster_url')
    u_movie.description = request.POST.get('description')
    # u_movie = Movie(title=title, audience=audience, genre=genre, score=score, poster_url=poster_url, description=description)
    u_movie.save()
    return redirect('/movies/')