from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserAPI.as_view()),
    path('login/kakao/', views.kakao_login, name='kakao_login'),
    path('login/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/', views.KakaoLogin.as_view()),
    path('kakaopay/', views.Kakaopay),
    path('kakaopay/approval/', views.KakaopayApproval)
]
