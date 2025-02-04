from django.contrib import admin
from .models import Genre, Writer, Fairytale, BookMark, Scenario, VoiceStorage
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name']


class WriterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']
    fields = ['user', 'name']


class FairytaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_pay']
    fields = ['title', 'summary', 'image', 'date', 'writer', 'Genre', 'is_pay']


class ScenarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'fairytale', 'content']
    fields = ['fairytale', 'content']


class VoiceStorageAdmin(admin.ModelAdmin):
    list_display = ['id', 'fairytale', 'scenario', 'voice_model']
    fields = ['fairytale', 'scenario' ,'voice_model', 'voice_file']

class BookMarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'fairytale', 'page', 'last_date']
    fields = ['user', 'fairytale', 'page']


admin.site.register(Genre, GenreAdmin)
admin.site.register(Writer, WriterAdmin)
admin.site.register(Fairytale, FairytaleAdmin)
admin.site.register(Scenario, ScenarioAdmin)
admin.site.register(VoiceStorage, VoiceStorageAdmin)
admin.site.register(BookMark, BookMarkAdmin)