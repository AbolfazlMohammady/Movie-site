from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tv_movie = Movie.objects.filter(category="Movie").order_by('id')
        context["tv_movie1"] = tv_movie[:4]
        context["tv_movie2"] = tv_movie[4:12]
        
        context["tv_serious"] = Movie.objects.filter(category="TV Shows").order_by('id')
        return context
    

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"
    context_object_name = "movie"

def search(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Movie.objects.filter(name__icontains=query)
    return render(request, 'movies/movies_search.html', {'results': results, 'query': query})

