# rest_framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from AI_PJT3 import settings
from .models import Subscribe
from .serializers import SubscribeSerializer, UserSerializer
import datetime
import json
import requests
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

admin_key = settings.env('ADMIN_KEY')
amount = int(4800)
tax_free_amount = int(0)
kakaopay_content_type = 'application/x-www-form-urlencoded;charset=utf-8'
kakaopay_headers = {
    'Authorization': "KakaoAK " + admin_key,
    'Content-type': kakaopay_content_type,
}


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
def kakaopay(request):
    subscribe = Subscribe.objects.filter(user=request.user).filter(end_date__gte=datetime.datetime.today()).filter(is_return=False)
    if subscribe:
        return Response('이미 이용권이 존재합니다!', status=status.HTTP_400_BAD_REQUEST)
    url = "https://kapi.kakao.com/v1/payment/ready"
    redirect_url = settings.env('PAY_REDIRECT_URL')
    approval_url = settings.env('PAY_APPROVAL_URL')
    params = {
        'cid': "TC0ONETIME", # 가맹점 코드, 테스트 코드
        'partner_order_id': '01', # 가맹점 주문번호, 테스트므로 임의값 지정
        'partner_user_id': '나랑노랑', # 가맹점 회원 id, 테스트므로 임의값 지정
        'item_name': '나랑노랑 이용권',
        'quantity': 1,
        'total_amount': amount,
        'tax_free_amount': tax_free_amount, # 상품 비과세 금액
        'approval_url': approval_url,
        'fail_url': redirect_url,
        'cancel_url': redirect_url,
    }
    res = requests.post(url, params=params, headers=kakaopay_headers)
    res = json.loads(res.text)
    return Response(res)    

@api_view(['POST'])
def kakaopay_approval(request):
    url = "https://kapi.kakao.com/v1/payment/approve"
    params = {
        "cid" : "TC0ONETIME",
        "tid" : request.data['tid'],
        "partner_order_id" : '01',
        "partner_user_id" : '나랑노랑',
        "pg_token" : request.data["pg_token"]
    }
    res = requests.post(url, headers=kakaopay_headers, params=params)
    res = res.json()

    subscribe = Subscribe()
    subscribe.create(request.user, request.data['tid'])

    return Response(res)

@api_view(['POST'])
def kakaopay_info(request):
    subscribe = Subscribe.objects.get(tid=request.data['tid'])
    url = "https://kapi.kakao.com/v1/payment/order"
    params = {
        "cid" : "TC0ONETIME",
        "tid" : subscribe.tid,
    }
    res = requests.post(url, headers=kakaopay_headers, params=params)
    res = res.json()
    return Response(res)

class SubscribeInfo(APIView):
    def get(self, request):
        subscribes = Subscribe.objects.filter(user=request.user)
        serializer = SubscribeSerializer(subscribes, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def kakaopay_refund(request):
    subscribe = Subscribe.objects.get(tid=request.data['tid'])
    url = "https://kapi.kakao.com/v1/payment/cancel"
    params = {
        "cid" : "TC0ONETIME",
        "tid" : subscribe.tid,
        'cancel_amount' : amount,
        "cancel_tax_free_amount" : tax_free_amount 
    }
    res = requests.post(url, headers=kakaopay_headers, params=params)
    res = res.json()

    subscribe.refund() 

    return Response(res)