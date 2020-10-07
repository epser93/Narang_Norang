# issue 정리
## 09.15

### server

django에서 보안을 위해 .env파일을사용해서 생겼던 문제

mysql에서 사용자를 USER라고 지정

AWS EV2에서 env('USER')를 가져오면 계속 ubuntu라고 나옴

기본적인 환경변수가 적용되어 있는걸로 예상됨

env파일에서 USER를 DB_USER로 변경함으로써 문제 해결

해결하는데 걸린시간 8시간...(mysql 유저변경, 권한설정, 자료조사 등..)