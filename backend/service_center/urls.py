from django.urls import path
from . import views

urlpatterns = [
    path('QnA/', views.QnAList.as_view()),
    path('QnA/<int:pk>/', views.QnADetail.as_view()),
    path('FaQ/', views.FaQList.as_view()),
    path('FaQ/<int:pk>/', views.FaQDetail.as_view())

]
