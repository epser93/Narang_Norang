from django.urls import path
from . import views

urlpatterns = [
    path('caption/', views.TrainCaption.as_view()),
    path('train/category/', views.TrainVoiceCategory.as_view()),
    path('train/category/<int:category_id>/', views.TrainVoiceCategoryDetail.as_view()),
    path('train/category/<int:category_id>/<int:caption_id>/', views.TrainAPI.as_view()),
    path('', views.VoiceModelAPI.as_view()),
    path('voice/<int:voice_id>/', views.VoiceModelDetailAPI.as_view())
]
