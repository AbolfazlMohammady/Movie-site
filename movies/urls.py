from django.urls import path

from .views import MovieListView, MovieDetailView , search, MovieListAllView, movie_chart_view

app_name = "movies"

urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list"),
    path('all/', MovieListAllView.as_view(), name='movie_all'), 
    path('chart/', movie_chart_view, name='movie_chart'),
    path("<int:pk>", MovieDetailView.as_view(), name="movie_detail"),
    path('search/', search, name='search'),
]
