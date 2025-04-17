import json
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
        
        context["tv_movie1"] = tv_movie[:6]
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


class MovieListAllView(ListView):
    model = Movie
    template_name = 'movies/all_movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5

    def get_queryset(self):
        return Movie.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = context['page_obj']  
        return context
    
def movie_chart_view(request):
    movies = Movie.objects.all().order_by('created_at')

    movie_names = [movie.name for movie in movies]
    movie_years = [movie.created_at.year for movie in movies if movie.created_at]

    chart_data = json.dumps({
        'labels': movie_names,
        'data': movie_years
    })

    return render(request, 'movies/movie_chart.html', {'chart_data': chart_data})