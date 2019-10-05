''' Importing Views '''
from . import views
from django.urls import path

app_name = 'movie'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search_results'),
    path('movie/<str:movie_name>/', views.getmovie, name='movie_desc'),
]