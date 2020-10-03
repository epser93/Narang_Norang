# REST API 명세서

| url                                             | GET                                             | POST                               | PUT                  | DELETE               |
| ----------------------------------------------- | ----------------------------------------------- | ---------------------------------- | -------------------- | -------------------- |
| accounts/login/                                 |                                                 | 로그인                             |                      |                      |
| accounts/user/                                  | 유저정보                                        |                                    | 유저정보수정         |                      |
| accounts/writer/                                | 작가정보(개인)                                  | 작가생성                           | 작가수정             | 작가삭제             |
| accounts/writer/<writer_id>/                    | 작가정보                                        |                                    |                      |                      |
| accounts/subscribe/                             | 정액권정보                                      | 정액권결제                         |                      | 정액권 환불          |
| books/fairytale/                                | 전체리스트                                      | 동화생성(작가만)                   |                      |                      |
| books/fairytale/<book_id>                       | 동화상세정보                                    |                                    | 동화수정(작가만)     |                      |
| books/fairytale/<book_id>/voice/<voice_model>/  | 동화책 대본과 소리데이터 가져오기               |                                    |                      |                      |
| books/genre/                                    | 장르목록                                        | 장르생성(관리자)                   | 장르수정(관리자)     | 장르삭제(관리자)     |
| books/favorite/                                 | 즐겨찾기목록                                    |                                    |                      | 전체삭제             |
| books/favorite/<book_id>/                       |                                                 | 즐겨찾기 생성                      |                      | 즐겨찾기 삭제        |
| books/bookmark/<book_id>/                       | 페이지정보 읽기                                 |                                    | 페이지정보 수정      |                      |
| service_center/FaQ/                             | 자주묻는 리스트                                 | 내용생성(관리자)                   |                      |                      |
| service_center/FaQ/<faq_id>                     | 상세글 조회                                     |                                    | 내용수정(관리자)     | 내용삭제(관리자)     |
| service_center/category/                        | 카테고리 목록                                   | 카테고리생성(관리자)               | 카테고리수정(관리자) | 카테고리삭제(관리자) |
| service_center/QnA/                             | 전체가져오기                                    | 생성                               |                      |                      |
| service_center/QnA/<qna_id>/                    | qna상세정보                                     |                                    | QnA 수정             | QnA 삭제             |
| service_center/QnA/<qna_id>/reply/              | 답글조회                                        | 답글생성                           | 답글수정             | 답글삭제             |
| voices/                                         | 내 계정에서 만든 목소리들 + 임대한 목소리(임대) |                                    |                      |                      |
| voices/voice/<voice_id>/                        |                                                 |                                    | 목소리 정보 수정     | 목소리 삭제          |
| voices/caption/                                 | 학습용 대본 조회                                |                                    |                      |                      |
| voices/rent/                                    | 목소리 임대 리스트                              | 목소리 임대 생성                   |                      | 목소리 임대 삭제     |
| voices/rent/<voice_id>/                         | 목소리 테스트 내용                              | 목소리 구매                        |                      |                      |
| voices/train/category/                          | 내가만든 카테고리 조회                          | 카테고리 생성                      |                      |                      |
| voices/train/category/<category_id>/            | 해당 카테고리 내용 조회                         | 모델학습시작(모두 채워져 있을때만) | 카테고리 수정        | 카테고리 삭제        |
| voices/train/category/<category_id>/<train_id>/ |                                                 | 데이터 추가                        |                      | 데이터 삭제          |



## 요청 응답방식

임시

### 소셜로그인 요청(브라우저에서 검색)

```
https://j3c206.p.ssafy.io/api/accounts/login/kakao/
```

- 응답

```json
{
    "access_token": "_V0DqReM7CNA2L4z5rBWyQxeO1AuJ6_dOLxYpQo9c00AAAF0uGG_Vg",
    "token_type": "bearer",
    "refresh_token": "QzA74l847etqy8tXTWOslO0J0OXbF5evk84XPwo9c00AAAF0uGG_VA",
    "expires_in": 21599,
    "scope": "profile",
    "refresh_token_expires_in": 5183999
}
```



### JWT 토큰 발급받기(POST)

```
https://j3c206.p.ssafy.io/api/accounts/kakao/
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
    "is_staff": false
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
    "is_staff": false
}
```



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
        "image": "/media/KakaoTalk_20200921_091027148.png"
    },
    {
        "id": 2,
        "title": "동화2",
        "image": "/media/KakaoTalk_20200921_091027148_D0qNP8G.png"
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
    "summary": "동화 줄거리",
    "image": "/media/KakaoTalk_20200921_091027148.png",
    "date": "2020-09-21",
    "writer": 1,
    "Genre": 1
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
        "scenario": {
            "content": "'옛날 어느 고을에 흥부와 놀부라는 형제가 살았어요',"
        },
        "voice_file": "/media/eval-135000-0.wav"
    },
    {
        "scenario": {
            "content": "'동생 흥부는 마음씨가 착하고 형 놀부는 맘대로 하는 심술쟁이 욕심꾸러기였어요',"
        },
        "voice_file": "/media/eval-135000-1.wav"
    },
    {
        "scenario": {
            "content": "'어느날 아버지가 병으로 앓아누어 돌아가시자 아버지에게서 물려받은 유산을 자기혼자 다 차지한 놀부는 동생 흥부를 쫒아냈어요',"
        },
        "voice_file": "/media/eval-135000-2.wav"
    },
    {
        "scenario": {
            "content": "'형님 겨울만 나게 해주십시오',"
        },
        "voice_file": "/media/eval-135000-3.wav"
    },
    {
        "scenario": {
            "content": "'이추운날 이어린것들을 두고 어디로 가라고 하십니까',"
        },
        "voice_file": "/media/eval-135000-4.wav"
    },
    {
        "scenario": {
            "content": "'더 이상 못봐준다니깐 난 너희 그많은 자식들만보면 소화가 안돼',"
        },
        "voice_file": "/media/eval-135000-5.wav"
    },
    {
        "scenario": {
            "content": "'몇일만이라도  아님 쌀이라도 주십시 형님',"
        },
        "voice_file": "/media/eval-135000-6.wav"
    },
    {
        "scenario": {
            "content": "'놀부는 간절히 부탁하는 흥부를 뿌리쳤어요',"
        },
        "voice_file": "/media/eval-135000-7.wav"
    },
    {
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

