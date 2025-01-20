from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template import loader
from .models import Movie, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["title", ]

    

def movie_chart_view(request):
    movies = Movie.objects.all()
    template = loader.get_template('admin/movie_chart.html')
    context = {
        'movies': movies,
    }
    return HttpResponse(template.render(context, request))

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "resolution",]
    list_filter = ["release", "category", "resolution", "assortment"]
    search_fields = ["name", "description"]
    ordering = ["release"]
    change_list_template = "admin/movie_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('movie-chart/', self.admin_site.admin_view(movie_chart_view), name='movie-chart'),
        ]
        return custom_urls + urls