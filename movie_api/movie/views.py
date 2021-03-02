from django.shortcuts import render
import requests
from movie_api.settings import API_KEY

# Create your views here.

def index(request):
    sender = {'index':True}
    return render(request, 'movie/main.html', sender)

def search(request):
    m = request.GET.get('q')
    url = 'http://www.omdbapi.com/?apikey='+ API_KEY
    params = {'s': m}
    r = requests.get(url, params=params)
    movie = r.json()
    if 'Error' in movie:
        sender = {'Error': True, 'search': m}
    else:
        sender = {'Error': False,'movie': movie,'search':m}
    return render(request, 'movie/main.html', sender)

def getmovie(request, movie_name):
    url = 'http://www.omdbapi.com/?apikey='+ API_KEY
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
        second = ['Plot','Language', 'Country', 'Released', 'BoxOffice', 'Production',  'Writer','Response',
         'Rated', 'DVD','Type', 'imdbID','imdbVotes', 'imdbRating', 'Metascore', 'Awards', 'Website']
        sender = {'movie': movie,'first':first,'second':second,'ratings':ratings}
    return render(request, 'movie/movie.html', sender)
