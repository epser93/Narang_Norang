# rest_framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from AI_PJT3 import settings
import requests
from rest_framework.response import Response

from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

client_id = settings.env('CLIENT_ID')
redirect_uri = "http://127.0.0.1:8000/api/accounts/login/callback"

# 인증 code 요청
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def kakao_login(request):
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")

# access token 받기
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def kakao_callback(request):
    response_code = request.GET.get('code')
    token = requests.post(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={response_code}")
    token = token.json()
    return Response(token)


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_data(request):
    print(request.user)
    return Response(True)