# Django와 Mysql연동하기



## 1. mysqlclient 설치하기

```bash
 pip install mysqlclient
```

- ubuntu일경우

```
sudo apt-get install libmysqlclient-dev
```







## 2. django settings.py 수정하기

- settings.py에 있는 DATABASES 를 수정해줘야 한다.
- 아래는 공식문서에 적혀있는 내용이다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}

# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
```

- 그리고 옵션에 아래와 같이 추가해야 한다고 적혀있다.

```python
SET sql_mode='STRICT_TRANS_TABLES'
```



- 나는 env파일을 사용하여 적용해 보았다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('PORT'),
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}


# .env 파일
NAME=DBNAME
DB_USER=DBUSER
PASSWORD=DBUSERPASSWORD
HOST=localhost
PORT=3306
```



## 3. 실행하기

- DB를 실행하고 django를 동작시키면 연결되는 것을 확인할 수 있다.
- DB를 연결하기 전에 DB는 먼저 생성해야 하는점을 유의해야 한다.



참조 : https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-notes

