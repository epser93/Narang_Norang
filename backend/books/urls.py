from django.urls import path
from . import views

urlpatterns = [
    path('fairytale/', views.FairytaleList.as_view()),
]
