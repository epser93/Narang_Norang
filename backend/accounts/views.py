# rest_framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework.response import Response
from AI_PJT3 import settings
import json

from .serializers import UserSerializer

import requests

from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

client_id = settings.env('CLIENT_ID')
if settings.DEBUG:
    redirect_uri = "http://127.0.0.1:8000/api/accounts/login/callback/"
else:
    redirect_uri = 'https://j3c206.p.ssafy.io/api/accounts/login/callback/'
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


class UserAPI(APIView):
    
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request, format=None):
        request.user.update(request.data)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

@api_view(['POST'])
def Kakaopay(request):
    url = "https://kapi.kakao.com/v1/payment/ready"
    redirect_url = settings.env('PAY_REDIRECT_URL')
    approval_url = settings.env('PAY_APPROVAL_URL')
    admin_key = settings.env('ADMIN_KEY')
    headers = {
        'Authorization': "KakaoAK " + admin_key,
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    params = {
        'cid': "TC0ONETIME", # 가맹점 코드, 테스트 코드
        'partner_order_id': '01', # 가맹점 주문번호, 테스트므로 임의값 지정
        'partner_user_id': '나랑노랑', # 가맹점 회원 id, 테스트므로 임의값 지정
        'item_name': '나랑노랑 이용권',
        'quantity': 1,
        'total_amount': 19800,
        'tax_free_amount': 0, # 상품 비과세 금액
        'approval_url': approval_url,
        'fail_url': redirect_url,
        'cancel_url': redirect_url,
    }
    res = requests.post(url, params=params, headers=headers)
    res = json.loads(res.text)
    return Response(res)    

@api_view(['POST'])
def KakaopayApproval(request):
    url = "https://kapi.kakao.com/v1/payment/approve"
    admin_key = settings.env('ADMIN_KEY')
    headers = {
        'Authorization': "KakaoAK " + admin_key,
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    params = {
        "cid" : "TC0ONETIME",
        "tid" : request.data['tid'],
        "partner_order_id" : '01',
        "partner_user_id" : '나랑노랑',
        "pg_token" : request.data["pg_token"]
    }
    res = requests.post(url, headers=headers, params=params)
    res = res.json()
    return Response(res)