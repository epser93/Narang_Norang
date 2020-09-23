from django.urls import path
from . import views

urlpatterns = [
    path('fairytale/', views.FairytaleList.as_view()),
    path('fairytale/<int:pk>/', views.FairytaleDetail.as_view()),
    path('genre/', views.GenreList.as_view()),
    path('favorite/', views.FavoriteAPI.as_view()),
    path('favorite/<int:pk>/', views.FavoriteAPI.as_view()),
]
