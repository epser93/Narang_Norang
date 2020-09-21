from django.contrib import admin
from .models import Genre, Writer, Fairytale, BookMark
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name']


class WriterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']
    fields = ['user', 'name']


class FairytaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    fields = ['title', 'summary', 'content', 'image', 'date', 'writer', 'Genre']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Writer, WriterAdmin)
admin.site.register(Fairytale, FairytaleAdmin)