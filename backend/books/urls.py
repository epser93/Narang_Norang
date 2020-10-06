from django.urls import path
from . import views

urlpatterns = [
    path('fairytale/', views.FairytaleList.as_view()),
    path('fairytale/<int:pk>/', views.FairytaleDetail.as_view()),
    path('fairytale/<int:pk>/voice/<int:model_pk>/', views.VoiceStoageAPI.as_view()),
    path('fairytale/search/<str:fairytale_name>/', views.FairytailSearch.as_view()),
    path('bookmark/', views.BookMarkAPI.as_view()),
    path('bookmark/<int:pk>/', views.BookmarkDetailAPI.as_view()),
    path('genre/', views.GenreList.as_view()),
    path('favorite/', views.FavoriteAPI.as_view()),
    path('favorite/<int:pk>/', views.FavoriteAPI.as_view()),
    path('scenario/<int:f_id>/', views.AddScenario.as_view()),
    path('voice_storage/<int:f_id>/<int:s_id>/<int:m_id>/', views.AddVoiceStorage.as_view()),
]
