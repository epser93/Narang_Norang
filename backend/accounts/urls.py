from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserAPI.as_view()),
    path('kakao/', views.KakaoLogin.as_view()),
    path('kakaopay/', views.kakaopay),
    path('kakaopay/approval/', views.kakaopay_approval),
    path('kakaopay/info/', views.kakaopay_info),
    path('kakaopay/refund/', views.kakaopay_refund),
    path('subscribes/', views.SubscribeInfo.as_view())
]
