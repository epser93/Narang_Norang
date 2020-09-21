# docker에서 mysql 설치하기

## 1. 홈페이지에 들어가서 docker를 설치

https://www.docker.com/get-started



## 2. docker image 가져오기

- cmd 창열기
- 도커허브에서 mysql 이미지 받아오기

```bash
docker pull mysql
```

- 다운로드된 도커 이미지 확인하기(mysql이 출력되면 정상)

```bash
docker images
```



## 3. mysql 컨테이너 설정하기

```bash
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=j3c206team --name ai_db mysql
```

- -d 는 컨테이너를 백그라운드에서 동작하는 어플리케이션으로 실행
  
- -p는 포트옵션으로 3306포트로 들어오면 컨테이너의 3306과 연결하겠다는 의미이다

- -e MYSQL_ROOT_PASSWORD=password 컨테이너를 생성하면서 환경변수를 설정, 여기서는 root password를 password로 설정한다라는 명령어이다.

* -name mysql_test 컨테이너의 이름을 mysql_test로 설정한다는 뜻이다.
* -v 옵션을 넣으면 공유할 디렉토리 설정이 가능하다. `-v [호스트 디렉토리]:[컨테이너 디렉토리]`

- 컨테이너가 정상적으로 생성되었는지 확인하기 위해 아래의 명령어로 확인한다.

```bash
docker ps -a
```

- STATUS 항목에 exit가 아니라 UP 시간이 나온다면 컨테이너가 동작
- ubuntu에서 터미널로 들어가고 싶다면 아래와 같은 명령어

```dockerfile
sudo docker exec -i -t ai_db bash
```



## 4. mysql 컨테이너 들어가보기

- docker프로세스 이미지에서 우클릭하여 Dashboard 클릭하기
- ai_db 컨테이너를 실행하고 CLI 들어가기

```bash
mysql -u root -p
```

- 위의 명령어를 사용한 뒤 생성시 사용한 password를 입력한다.





## 5. 권한 부여하기

- root 계정은 DBA가 사용하는 것이고 보통은 권한을 부여받은 유저를 받게된다.
- develop라는 유저 생성하기

```mysql
#CREATE USER 'username'@'%' IDENTIFIED BY 'password';
CREATE USER 'developer'@'%' IDENTIFIED BY 'j3c206team';
```

- developer에게 모든 권한 부여하기

```mysql
GRANT ALL PRIVILEGES ON *.* TO 'developer'@'%';
```

- 이후부터는 root가 아닌 develop를 이용하여 mysql에 접속한다.

```mysql
quit
mysql -u developer -p
```



## 6. DB생성하기

- mysql내부에 여러개의 DB를 만들 수가 있다.
- 데이터베이스를 조회하는 목록은 아래와 같다.

```mysql
show databases;
```

- 우리는 사용해야하는 DB를 따로만들어 줘야한다.

```mysql
#CREATE DATABASE dbname;
CREATE DATABASE ai_db;
```

- 특정한 DB를 사용하고 싶다면 사용하겠다고 선언을 해야한다.

```mysql
#use dbname;
use ai_db;
```



## 7.TABLE 확인하기

- 해당 DB에 어떠한 테이블이 있는지 확인하기 위한 명령어는 아래와 같다.

```mysql
show tables;
```

- 여기서는 sql명령어를 이용하여 원하는 명령을 내릴 수 있다.





## 8. docker 이미지 저장하기

- 작업한 내용을 컨테이너화 하고 싶다면 commit 명령어를 이용하여 저장이 가능하다.

```dockerfile
docker commit <컨테이너이름> <저장할 이미지 이름:태그이름>
```

- image에 태그를 달고싶다면 commit을 할때 이용하거나 아래와 같이 사용가능하다.

```dockerfile
docekr tag <이미지 이름> <your_docker_id>/<컨테이너이름:태그>
```



## 9. docker image 올리기

- 이미지를 만들었으면 docker hub에 이미지를 올려야 한다.
- docker hub에 repository를 만든다.
- 올려야할 이미지와 동일한이름의 repository면 된다.(혹은 반대던가)

- repository를 만들면 사이트 우측에 아래와 같이 적으라 나온다.

```dockerfile
docker push <your_docker_id>/<컨테이너이름:태그>
```





## 10. docker 이미지 삭제하기

- 이미지가 필요없어졌다면 삭제할때가 생긴다. 명령어는 아래와 같다.

```dockerfile
docker rmi <image name>
```



## 11.  ubuntu에서 docker 설치하기

- 아래와 같은 명령어를 순서대로 입력한다.

```bash
sudo apt update

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```



## 12. 데이터 백업/복구 하기

- 데이터를 백업할때는 아래와 같은 명령어를 이용한다.
  - window의 경우

  - ```bash
    docker exec ai_db sh -c 'exec mysqldump --all-databases -u root -p"$MYSQL_ROOT_PASSWORD"' > "D:\mysql\backup\data.sql"
    ```

  - ubuntu의 경우

  - ```bash
    docker exec some-mysql sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /some/path/on/your/host/all-databases.sql
    ```

- 데이터를 복구할때는 아래와 같은 명령어를 이용한다.

  - 할때 아스키코드 에러가 난다면 메모장으로 utf-8로 인코딩 변경을 한다.

```bash
docker exec -i ai__db sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < D:\mysql\backup\data.sql
```



## 13. docker 컨테이너 명령어

실행

```bash
sudo docker start <컨테이너 이름 혹은 아이디>
```

재시작

```bash
sudo docker restart <컨테이너 이름 혹은 아이디>
```

중지

```bash
sudo docker stop <컨테이너 이름 혹은 아이디>
```

삭제

```bash
sudo docker rm <컨테이너 이름 혹은 아이디>
```

접속

```bash

```

