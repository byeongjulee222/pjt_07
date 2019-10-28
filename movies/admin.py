from django.contrib import admin
from .models import Movie, Genre, Review

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'audience', 'poster_url', 'description', 'genre_id')

admin.site.register(Movie, MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Genre, GenreAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'score', 'movie_id', 'user_id')

admin.site.register(Review)
