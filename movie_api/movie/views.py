from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
import requests
# Create your views here.
def index(request):
    sender = {'index':True}
    return render(request, 'movie/main.html', sender)

def search(request):
    m = request.GET.get('q')
    url = 'http://www.omdbapi.com/?apikey=f8f4f680'
    params = {'s': m}
    r = requests.get(url, params=params)
    movie = r.json()
    print(movie)
    if 'Error' in movie:
        sender = {'Error': True, 'search': m}
    else:
        sender = {'Error': False,'movie': movie,'search':m}
    return render(request, 'movie/main.html', sender)

def getmovie(request, movie_name):
    url = 'http://www.omdbapi.com/?apikey=f8f4f680' 
    params = {'t':movie_name}
    r = requests.get(url, params=params)
    movie = r.json()
    if 'Error' in movie:
        sender = {'Error': True, 'search': movie_name}
    else:
        first = ['Title','Year','Actors','Runtime','Genre','Director']
        try:
            ratings = movie['Ratings']
        except Exception:
            ratings = []
        print(movie_name)
        second = ['Plot','Language', 'Country', 'Released', 'BoxOffice', 'Production',  'Writer','Response',
         'Rated', 'DVD','Type', 'imdbID','imdbVotes', 'imdbRating', 'Metascore', 'Awards', 'Website']
        sender = {'movie': movie,'first':first,'second':second,'ratings':ratings}
    return render(request, 'movie/movie.html', sender)
