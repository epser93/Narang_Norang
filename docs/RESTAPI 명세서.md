# REST API 명세서

| url                                               | GET                                             | POST                               | PUT                  | DELETE               |
| ------------------------------------------------- | ----------------------------------------------- | ---------------------------------- | -------------------- | -------------------- |
| accounts/login/                                   |                                                 | 로그인                             |                      |                      |
| accounts/user/                                    | 유저정보                                        |                                    | 유저정보수정         |                      |
| accounts/subscribe/                               | 정액권정보                                      | 정액권결제                         |                      | 정액권 환불          |
| books/fairytale/                                  | 전체리스트                                      |                                    |                      |                      |
| books/fairytale/search/<fairytale_name>/          | 동화책 검색                                     |                                    |                      |                      |
| books/fairytale/<book_id>                         | 동화상세정보                                    |                                    |                      |                      |
| books/fairytale/<book_id>/voice/<voice_model>/    | 동화책 대본과 소리데이터 가져오기               |                                    |                      |                      |
| books/genre/                                      | 장르목록                                        | 장르생성(관리자)                   | 장르수정(관리자)     | 장르삭제(관리자)     |
| books/favorite/                                   | 즐겨찾기목록                                    |                                    |                      | 전체삭제             |
| books/favorite/<book_id>/                         |                                                 | 즐겨찾기 생성                      |                      | 즐겨찾기 삭제        |
| books/bookmark/                                   | 내가 읽은 책 목록                               |                                    |                      |                      |
| books/bookmark/<book_id>/                         | 페이지정보 읽기                                 | 페이지 정보 등록                   |                      |                      |
| service_center/FaQ/                               | 자주묻는 리스트                                 | 내용생성(관리자)                   |                      |                      |
| service_center/FaQ/<faq_id>                       | 상세글 조회                                     |                                    | 내용수정(관리자)     | 내용삭제(관리자)     |
| service_center/category/                          | 카테고리 목록                                   | 카테고리생성(관리자)               | 카테고리수정(관리자) | 카테고리삭제(관리자) |
| service_center/QnA/                               | 전체가져오기                                    | 생성                               |                      |                      |
| service_center/QnA/<qna_id>/                      | qna상세정보                                     |                                    | QnA 수정             | QnA 삭제             |
| service_center/QnA/<qna_id>/reply/                | 답글조회                                        | 답글생성                           | 답글수정             | 답글삭제             |
| voices/                                           | 내 계정에서 만든 목소리들 + 임대한 목소리(임대) |                                    |                      |                      |
| voices/voice/<voice_id>/                          |                                                 |                                    | 목소리 정보 수정     | 목소리 삭제          |
| voices/caption/                                   | 학습용 대본 조회                                |                                    |                      |                      |
| voices/train/category/                            | 내가만든 카테고리 조회                          | 카테고리 생성                      |                      |                      |
| voices/train/category/<category_id>/              | 해당 카테고리 내용 조회                         | 모델학습시작(모두 채워져 있을때만) | 카테고리 수정        | 카테고리 삭제        |
| voices/train/category/<category_id>/<caption_id>/ |                                                 | 녹음 목소리 추가                   |                      | 녹음 목소리 삭제     |



## Accounts

### 카카오로그인하기 - JWT 토큰 발급받기(POST)

```
https://j3c206.p.ssafy.io/api/accounts/login/
```

- BODY

```json
{
    "access_token": "_V0DqReM7CNA2L4z5rBWyQxeO1AuJ6_dOLxYpQo9c00AAAF0uGG_Vg"
}
```

- 응답

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Ilx1YWU0MFx1YzcyMFx1YWUzMCIsImV4cCI6MTYwMDkwNzg3NCwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTYwMDgyMTQ3NH0.ukN-C1aUtBsqP8yoIJBl4MUROXly_Y-1WhCuNaV-XHU",
    "user": {
        "pk": 2,
        "username": "김유기",
        "email": "",
        "first_name": "",
        "last_name": ""
    }
}
```



### 유저정보 검색(GET)

```
https://j3c206.p.ssafy.io/api/accounts/user/
```

- 응답

```json
{
    "id": 2,
    "username": "김유기",
    "balance": 0,
    "first_name": "mungto",
    "is_staff": false,
    "is_subscribe" : false,
    "current_voice": 1
}
```



### 유저정보 수정(PUT)

```
https://j3c206.p.ssafy.io/api/accounts/user/
```

- BODY

```json
{
    "nick_name": "mungto123"
}
```

- 응답

```json
{
    "id": 2,
    "username": "김유기",
    "balance": 0,
    "first_name": "mungto123",
    "is_staff": false,
    "is_subscribed": false
}
```



## 카카오페이

> 결제 준비 -> 결제 승인 순서로 진행됩니다.

### 페이 결제 준비 (POST)

```
https://j3c206.p.ssafy.io/api/accounts/kakaopay/
```

- 응답

```json
{
    "tid": "T2814609304915267875",
    "tms_result": false,
    "next_redirect_app_url": "https://mockup-pg-web.kakao.com/v1/6238f4e724b1247f0407bfe47caee1177a113682a0bf094e3195138ce51e0716/aInfo",
    "next_redirect_mobile_url": "https://mockup-pg-web.kakao.com/v1/6238f4e724b1247f0407bfe47caee1177a113682a0bf094e3195138ce51e0716/mInfo",
    "next_redirect_pc_url": "https://mockup-pg-web.kakao.com/v1/6238f4e724b1247f0407bfe47caee1177a113682a0bf094e3195138ce51e0716/info",
    "android_app_scheme": "kakaotalk://kakaopay/pg?url=https://mockup-pg-web.kakao.com/v1/6238f4e724b1247f0407bfe47caee1177a113682a0bf094e3195138ce51e0716/order",
    "ios_app_scheme": "kakaotalk://kakaopay/pg?url=https://mockup-pg-web.kakao.com/v1/6238f4e724b1247f0407bfe47caee1177a113682a0bf094e3195138ce51e0716/order",
    "created_at": "2020-10-06T19:21:36"
}
```

> next_redirect_pc_url 로 리다이렉팅 시키시면 결제 페이지로 이동이 됩니다!
>
> tid를 저장해주세요



### 페이 결제 승인 (POST)

```
https://j3c206.p.ssafy.io/api/accounts/kakaopay/approval/
```

- body

```
{
   "tid" : 준비단계에서 나온 tid,
   "pg_token" : 리다이렉트 된 결제 진행 페이지의 쿼리스트링
}
```

- 응답

```json
aid: "A2814600169520689529"
amount:{
	discount: 0
	point: 0
	tax_free: 0
	total: 4800
	vat: 436
}
approved_at: "2020-10-06T18:46:17"
cid: "TC0ONETIME"
created_at: "2020-10-06T18:45:55"
item_name: "나랑노랑 이용권"
partner_order_id: "01"
partner_user_id: "나랑노랑"
payment_method_type: "MONEY"
quantity: 1
tid: "T2814600109390348074"
```



### 주문 정보 보기 (POST)

```
https://j3c206.p.ssafy.io/api/accounts/kakaopay/info/
```

- body

```
{
	"tid" : tid
}
```

- 응답

```json
amount:{
	discount: 0
	point: 0
	tax_free: 0
	total: 4800
	vat: 436
}
approved_at: "2020-10-06T18:46:17"
cancel_available_amount:{
	discount: 0
	point: 0
	tax_free: 0
	total: 4800
	vat: 436
}
canceled_amount: {total: 0, tax_free: 0, vat: 0, point: 0, discount: 0}
cid: "TC0ONETIME"
created_at: "2020-10-06T18:45:55"
item_name: "나랑노랑 이용권"
partner_order_id: "01"
partner_user_id: "나랑노랑"
payment_action_details: [{…}]
payment_method_type: "MONEY"
quantity: 1
status: "SUCCESS_PAYMENT"
tid: "T2814600109390348074"
```



### 페이 환불하기 (POST)

```
https://j3c206.p.ssafy.io/api/accounts/kakaopay/refund/
```

- body

```json
{
	"tid" : tid
}
```

- 응답

```json
aid: "A2814612835378385197"
amount: {total: 4800, tax_free: 0, vat: 436, point: 0, discount: 0}
approved_at: "2020-10-06T18:46:17"
approved_cancel_amount: {total: 4800, tax_free: 0, vat: 436, point: 0, discount: 0}
cancel_available_amount: {total: 0, tax_free: 0, vat: 0, point: 0, discount: 0}
canceled_amount: {total: 4800, tax_free: 0, vat: 436, point: 0, discount: 0}
canceled_at: "2020-10-06T19:35:18"
cid: "TC0ONETIME"
created_at: "2020-10-06T18:45:55"
item_name: "나랑노랑 이용권"
partner_order_id: "01"
partner_user_id: "나랑노랑"
payment_method_type: "MONEY"
quantity: 1
status: "CANCEL_PAYMENT"
tid: "T2814600109390348074"
```



### 이용권 결제 내역 보기 (GET)

```
https://j3c206.p.ssafy.io/api/accounts/subscribes/
```

- 응답

```json
[
    {
        "id": 8,
        "start_date": "2020-10-06",
        "end_date": "2020-10-05",
        "tid": "T2814596780790693638",
        "is_return": true
    },
    {
        "id": 10,
        "start_date": "2020-10-06",
        "end_date": "2020-10-05",
        "tid": "T2814599443670417184",
        "is_return": true
    },
    {
        "id": 11,
        "start_date": "2020-10-06",
        "end_date": "2020-10-05",
        "tid": "T2814600109390348074",
        "is_return": true
    }
]
```



## 동화책 관련

### 동화책 리스트 받아오기(GET)

```
https://j3c206.p.ssafy.io/api/books/fairytale/
```

- 응답

```json
[
    {
        "id": 1,
        "title": "동화1",
        "image": "/media/KakaoTalk_20200921_091027148.png",
        "is_pay": true
    },
    {
        "id": 2,
        "title": "동화2",
        "image": "/media/KakaoTalk_20200921_091027148_D0qNP8G.png",
        "is_pay": false
    }
]
```



### 동화책 검색 (GET)

```
https://j3c206.p.ssafy.io/api/books/fairytale/search/<str:fairytale_name>/
```

- 응답

```json
[
    {
        "id": 3,
        "title": "헨젤과 그레텔",
        "image": "/media/Naive_jDJezuX.PNG",
        "is_pay": false
    }
]
```



### 동화책 상세조회(GET)

```
https://j3c206.p.ssafy.io/api/books/fairytale/<int:id>/
```

- 응답

```json
{
    "id": 1,
    "title": "동화1",
    "summary": "동화1입니다.",
    "image": "/media/Naive.PNG",
    "date": "2020-09-21",
    "writer": 1,
    "Genre": 1,
    "is_liked": true
}
```



### 동화책 대본과 음성데이터 가져오기(GET)

```
https://j3c206.p.ssafy.io/api/books/fairytale/<int:fairytale_id>/voice/<int:voice_model_id>/
```

- 응답

```json
[
    {
        "id": 5,
        "scenario": {
            "content": "'옛날 어느 고을에 흥부와 놀부라는 형제가 살았어요',"
        },
        "voice_file": "/media/eval-135000-0.wav"
    },
    {
        "id": 6,
        "scenario": {
            "content": "'동생 흥부는 마음씨가 착하고 형 놀부는 맘대로 하는 심술쟁이 욕심꾸러기였어요',"
        },
        "voice_file": "/media/eval-135000-1.wav"
    },
    {
        "id": 7,
        "scenario": {
            "content": "'어느날 아버지가 병으로 앓아누어 돌아가시자 아버지에게서 물려받은 유산을 자기혼자 다 차지한 놀부는 동생 흥부를 쫒아냈어요',"
        },
        "voice_file": "/media/eval-135000-2.wav"
    },
    {
        "id": 8,
        "scenario": {
            "content": "'형님 겨울만 나게 해주십시오',"
        },
        "voice_file": "/media/eval-135000-3.wav"
    },
    {
        "id": 9,
        "scenario": {
            "content": "'이추운날 이어린것들을 두고 어디로 가라고 하십니까',"
        },
        "voice_file": "/media/eval-135000-4.wav"
    },
    {
        "id": 10,
        "scenario": {
            "content": "'더 이상 못봐준다니깐 난 너희 그많은 자식들만보면 소화가 안돼',"
        },
        "voice_file": "/media/eval-135000-5.wav"
    },
    {
        "id": 11,
        "scenario": {
            "content": "'몇일만이라도  아님 쌀이라도 주십시 형님',"
        },
        "voice_file": "/media/eval-135000-6.wav"
    },
    {
        "id": 12,
        "scenario": {
            "content": "'놀부는 간절히 부탁하는 흥부를 뿌리쳤어요',"
        },
        "voice_file": "/media/eval-135000-7.wav"
    },
    {
        "id": 13,
        "scenario": {
            "content": "'흥부는 아내와 여러 자식들을 거느니고 다 무너져가는 초가집에서 헐벗은 채',"
        },
        "voice_file": "/media/eval-135000-8.wav"
    }
]
```



### 동화책 장르 리스트 조회 (GET)

```
https://j3c206.p.ssafy.io/api/books/genre/
```

- 응답

```json
[
    {
        "id": 1,
        "name": "액션"
    },
    {
        "id": 2,
        "name": "이솝우화"
    },
    {
        "id": 3,
        "name": "드라마틱"
    }
]
```



### Favorite 조회(GET)

```
https://j3c206.p.ssafy.io/api/books/favorite/
```

- 응답

```json
[
    {
        "id": 1,
        "title": "동화1",
        "image": "/media/KakaoTalk_20200921_091027148.png"
    }
]
```



### Favorite 추가(POST)

```
https://j3c206.p.ssafy.io/api/books/favorite/<int:id>/
```

- 응답

```json
"추가완료"
or
"이미 추가되어 있습니다."
```



### Favorite 삭제(DELETE)

```
https://j3c206.p.ssafy.io/api/books/favorite/<int:id>/
```

- 응답

```json
"삭제완료"
or
"이미 삭제되어 있습니다."
```

### 북마크한 동화 목록 가져오기 (GET)

```
https://j3c206.p.ssafy.io/api/books/bookmark/
```

- 응답

```json
[
    {
        "id": 1,
        "fairytale": {
            "id": 1,
            "title": "햇님과 바람의 내기",
            "image": "/media/KakaoTalk_20200921_091027148.png"
        }
    }
]
```



### 북마크 가져오기 (GET)

```
https://j3c206.p.ssafy.io/api/books/bookmark/<int:book_id>
```

- 응답

```json
[
    {
        "id": 1,
        "page": 2
    }
]
```

> page가 북마크 번호입니다!



### 북마크 저장하기 (POST)

```
https://j3c206.p.ssafy.io/api/books/bookmark/<int:book_id>
```

- body

```json
{
    "id" : 2
}
```

> 해당 대본 id 번호를 보내주시면 됩니다.

- 응답

```json
'북마크 등록 완료'
```



## 고객센터 - Q&A

### Q&A 리스트 가져오기(GET)

```
https://j3c206.p.ssafy.io/api/service_center/QnA/
```

- 응답

```json
[
    {
        "id": 3,
        "title": "test123",
        "content": "test123",
        "create_date": "2020-09-22",
        "is_answer": false,
        "user": {
            "id": 2,
            "username": "김유기",
            "balance": 0,
            "first_name": "mungto123",
            "is_staff": false
        },
        "qna_reply" : []
    }
]
```



### Q&A 작성하기 (POST)

```
https://j3c206.p.ssafy.io/api/service_center/QnA/
```

- BODY

```json
{
    "title": "Q&A 제목",
    "content": "Q&A 내용"
}
```

- 응답

```json
{
    "id": 4,
    "title": "Q&A 제목",
    "content": "Q&A 내용",
    "create_date": "2020-09-23",
    "is_answer": false,
    "user": {
        "id": 2,
        "username": "김유기",
        "balance": 0,
        "first_name": "mungto123",
        "is_staff": false
    },
    "qna_reply" : []
}
```



- QNA 상세조회(GET)

```
https://j3c206.p.ssafy.io/api/service_center/QnA/<int:id>/
```

- 응답

```json
{
    "id": 4,
    "title": "Q&A 제목",
    "content": "Q&A 내용",
    "create_date": "2020-09-23",
    "is_answer": false,
    "user": {
        "id": 2,
        "username": "김유기",
        "balance": 0,
        "first_name": "mungto123",
        "is_staff": false
    },
    "qna_reply" : []
}
```



### Q&A 수정하기(PUT)

```
https://j3c206.p.ssafy.io/api/service_center/QnA/<int:id>/
```

- BODY

```json
{
    "title": "Q&A 제목수정",
    "content": "Q&A 내용수정"
}
```

- 응답

```json
{
    "id": 4,
    "title": "Q&A 제목수정",
    "content": "Q&A 내용수정",
    "create_date": "2020-09-23",
    "is_answer": false,
    "user": {
        "id": 2,
        "username": "김유기",
        "balance": 0,
        "first_name": "mungto123",
        "is_staff": false
    },
    qna_reply : []
}
```



### Q&A 삭제하기(DELETE)

```
https://j3c206.p.ssafy.io/api/service_center/QnA/<int:id>/
```

```json
"삭제완료"
```



### QnA 답글 생성 (POST)

```
https://j3c206.p.ssafy.io/api/service_center/QnA/<int:qna_id>/reply
```

- body

```json
{
    "content": "답글",
}
```

- 응답

```json
{
    "id": 14,
    "content": "답글",
    "create_date": "2020-09-24"
}
```



### QnA 답글 수정 (PUT)

```
https://j3c206.p.ssafy.io/api/service_center/QnA/<int:qna_id>/reply
```

- body

```json
{
    "content": "수정"
}
```

- 응답

```json
{
    "id": 14,
    "content": "수정",
    "create_date": "2020-09-24"
}
```



### QnA 답글 삭제 (DELETE)

```
https://j3c206.p.ssafy.io/api/service_center/QnA/<int:qna_id>/reply
```

- 응답

```json
"삭제완료"
```



## 고객센터 - FaQ

### FaQ 리스트 전체 조회(GET)

```
https://j3c206.p.ssafy.io/api/service_center/FaQ/
```

- 응답

```json
[    
	{
        "id": 1,
        "title": "1번",
        "content": "1번",
        "faq_category": {
            "id": 1,
            "name": "1번"
        }
    }
]
```



### FaQ 생성하기 (POST)

> 관리자만 가능

```
https://j3c206.p.ssafy.io/api/service_center/FaQ/
```

- body

```json
{
    "title": "FaQ 제목",
    "content": "FaQ 내용",
    "faq_category" : 3(카테고리id)
}
```

- 응답

```json
{
    "id": 4,
    "title": "FaQ 제목",
    "content": "FaQ 내용",
    "faq_category": {
        "id": 3,
        "name": "3번"
    }
}
```



### FaQ 수정하기(PUT)

> 관리자만 가능

```
https://j3c206.p.ssafy.io/api/service_center/FaQ/<int:faq_id>/
```

- body

```json
{
    "title": "FaQ 제목수정",
    "content": "FaQ 내용수정",
    "faq_category" : 2(카테고리id)
}
```

- 응답

```json
{
    "id": 4,
    "title": "FaQ 제목수정",
    "content": "FaQ 내용수정",
    "faq_category": {
        "id": 2,
        "name": "2번"
    }
}
```



### FaQ 삭제하기 (DELETE)

> 관리자만 가능

```
https://j3c206.p.ssafy.io/api/service_center/FaQ/<int:faq_id>/
```

- 응답

```json
"삭제완료"
```



### FaQ Detail 조회 (GET)

```
https://j3c206.p.ssafy.io/api/service_center/FaQ/<int:faq_id>/
```

- 응답

```json
{
    "id": 2,
    "title": "2번",
    "content": "2번",
    "faq_category": {
        "id": 2,
        "name": "2번"
    }
}
```



## 녹음, 학습 관련

### 학습용 대본 불러오기 (GET)

```
https://j3c206.p.ssafy.io/api/voices/caption
```

- 응답

```json
[
    {
        "id": 1,
        "content": "'옛날 어느 고을에 흥부와 놀부라는 형제가 살았어요'"
    },
    {
        "id": 2,
        "content": "'동생 흥부는 마음씨가 착하고 형 놀부는 맘대로 하는 심술쟁이 욕심꾸러기였어요'"
    }
]
```



### 훈련용 목소리 카테고리 전체 조회(GET)

```
https://j3c206.p.ssafy.io/api/voices/train/category
```

- 응답

```json
[
    {
        "id": 3,
        "name": "아나운서"
    },
    {
        "id": 4,
        "name": "엄마"
    }
]
```



### 훈련용 목소리 카테고리 생성 (POST)

```
https://j3c206.p.ssafy.io/api/voices/train/category
```

- body

```json
{
    "name": "엄마"
}
```

- 응답

```json
[
    {
        "name": "엄마"
    }
]
```



### 훈련용 목소리 카테고리 상세 조회 (GET)

```
https://j3c206.p.ssafy.io/api/voices/train/category/<int:category_id>
```

- 응답

```json
[
    {
        "id": 1,
        "voice_category": {
            "id": 4,
            "name": "친구A"
        },
        "train_file": "/media/%EC%A0%84%EC%82%B0%EC%A7%81_%EA%B3%B5%EB%B6%80_-_%EB%B3%B5%EC%82%AC%EB%B3%B8.wmv",
        "caption": {
            "id": 1,
            "content": "'옛날 어느 고을에 흥부와 놀부라는 형제가 살았어요'"
        }
    }
]
```





### 훈련용 목소리 카테고리 삭제 (DELETE)

```
https://j3c206.p.ssafy.io/api/voices/train/category/<int:category_id>
```

- 응답

```json
"삭제완료"
```



### 훈련용 목소리 카테고리 수정 (PUT)

```json
https://j3c206.p.ssafy.io/api/voices/train/category/<int:category_id>
```

- body

```json
{
    "name": "친구A"
}
```

- 응답

```json
{
    "id": 4,
    "name": "친구A"
}
```



### 목소리 학습 시작하기 (POST)

```
https://j3c206.p.ssafy.io/api/voices/train/category/<int:category_id>
```

- 응답

```json
// 녹음을 덜 했을 때
"녹음이 더 필요합니다" >> 400 BAD Request

// 모든 대본을 녹음했을 때 학습시작
"학습시작"

// 학습중일 때 재요청이 들어온다면
"학습중입니다."
```



## 훈련된 목소리 모델 관련

### 사용 가능 목소리 모델 리스트 조회 (GET)

```
https://j3c206.p.ssafy.io/api/voices/
```

- 응답

```json
[
    {
        "id": 2,
        "name": "아빠"
    },
    {
        "id": 3,
        "name": "엄마"
    }
]
```



### 사용할 모델 변경(POST)

```
https://j3c206.p.ssafy.io/api/voices/voice/<int:voice_id>/
```

- 응답

```json
"변경완료" > 1번 혹은 자신 모델일경우

"변경 불가/실패" > 자신이 사용못하는 모델일 경우
```



### 목소리 모델 이름 수정 (PUT)

```
https://j3c206.p.ssafy.io/api/voices/voice/<int:voice_id>/
```

- body

```json
{
    "name": "수정할 이름"
}
```

- 응답

```json
{
    "id": 2,
    "name": "수정할 이름"
}
```



### 목소리 모델 삭제 (DELETE)

```
https://j3c206.p.ssafy.io/api/voices/voice/<int:voice_id>/
```

- 응답

```json
'삭제완료'
```



## 목소리 음성 파일

### 목소리 음성 파일 추가하기 (POST)

```
https://j3c206.p.ssafy.io/api/voices/train/category/<category_id>/<caption_id>/
```

- body

```
form-data

file : 음성파일
```

- 응답

```json
'저장완료'
```



### 목소리 음성 파일 삭제하기 (DELETE)

```
https://j3c206.p.ssafy.io/api/voices/train/category/<category_id>/<caption_id>/
```

- 응답

```json
'삭제완료'
```

