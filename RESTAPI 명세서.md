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
| books/genre/                                    | 장르목록                                        | 장르생성(관리자)                   | 장르수정(관리자)     | 장르삭제(관리자)     |
| books/favorite/                                 | 즐겨찾기목록                                    |                                    |                      | 전체삭제             |
| books/favorite/<book_id>/                       |                                                 | 즐겨찾기 생성                      |                      | 즐겨찾기 삭제        |
| books/bookmark/<book_id>/                       | 페이지정보 읽기                                 |                                    | 페이지정보 수정      |                      |
| service_center/FaQ/                             | 자주묻는 리스트                                 | 내용생성(관리자)                   | 내용수정(관리자)     | 내용삭제(관리자)     |
| service_center/category/                        | 카테고리 목록                                   | 카테고리생성(관리자)               | 카테고리수정(관리자) | 카테고리삭제(관리자) |
| service_center/QnA/                             | 전체가져오기                                    | 생성                               |                      |                      |
| service_center/QnA/<qna_id>/                    | qna상세정보                                     |                                    | QnA 수정             | QnA 삭제             |
| service_center/QnA/<qna_id>/reply/              | 답글조회                                        | 답글생성                           | 답글수정             | 답글삭제             |
| voices/                                         | 내 계정에서 만든 목소리들 + 임대한 목소리(임대) |                                    |                      |                      |
| voices/voice/<voice_id>/                        | 목소리 모델                                     |                                    | 목소리 정보 수정     | 목소리 삭제          |
| voices/caption/                                 | 캡션리스트                                      |                                    |                      |                      |
| voices/rent/                                    | 목소리 임대 리스트                              | 목소리 임대 생성                   |                      | 목소리 임대 삭제     |
| voices/rent/<voice_id>/                         | 목소리 테스트 내용                              | 목소리 구매                        |                      |                      |
| voices/train/category/                          | 내가만든 카테고리 조회                          | 카테고리 생성                      |                      |                      |
| voices/train/category/<category_id>/            | 해당 카테고리 내용 조회                         | 모델학습시작(모두 채워져 있을때만) | 카테고리 수정        | 카테고리 삭제        |
| vocies/train/category/<category_id>/<train_id>/ |                                                 | 데이터 추가                        |                      | 데이터 삭제          |

