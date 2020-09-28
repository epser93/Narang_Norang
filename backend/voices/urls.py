from django.urls import path
from . import views

urlpatterns = [
    path('train/category/<int:category_id>/<int:caption_id>/', views.TrainAPI.as_view()),

]
