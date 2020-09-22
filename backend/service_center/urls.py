from django.urls import path
from . import views

urlpatterns = [
    path('QnA/', views.QnAList.as_view()),
    path('QnA/<int:pk>/', views.QnADetail.as_view()),

]
