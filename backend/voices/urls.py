from django.urls import path
from . import views

urlpatterns = [
    path('train/category/', views.TrainVoiceCategory.as_view()),
    path('train/category/<int:category_id>/', views.TrainVoiceCategoryDetail.as_view())
]
