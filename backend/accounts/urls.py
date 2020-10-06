from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserAPI.as_view()),
    path('login/kakao/', views.kakao_login, name='kakao_login'),
    path('login/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/', views.KakaoLogin.as_view()),
    path('kakaopay/', views.kakaopay),
    path('kakaopay/approval/', views.kakaopay_approval),
    path('kakaopay/info/', views.kakaopay_info),
    path('kakaopay/refund/', views.kakaopay_refund),
    path('subscribes/', views.SubscribeInfo.as_view())
]
