# gunicorn

## 1. gunicorn 설치

```bash
pip install gunicorn
```



## 2. gunicorn 셋팅

settings.py 에서 정적파일 저장할 경로 추가

```python
STATIC_ROOT = '/static/'
```



manage.py가 있는 경로에서 아래와 같이 실행

```bash
python manage.py collectstatic
```



아래경로에 파일 생성

```bash
/etc/systemd/system/gunicorn.service
```



WorkingDirectory에는 manage.py가 있는 경로를 적어준다.

ExecStart에는 gunicorn이 설치된 경로를 적어준다. (venv라면 venv 경로로)

--workers 는 gunicorn으로 동작시킬 프로세스 수이다.

--workers 뒤에 프로젝트명.wsgi:application로 작성한다.

```shell
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/project/s03p22c206/backend
ExecStart=/home/ubuntu/anaconda3/envs/AI/bin/gunicorn --workers 3 AI_PJT3.wsgi:application

[Install]
WantedBy=multi-user.target

```

## 3. gunicorn 명령어

서비스 등록

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

서비스 재시작

```bash
sudo systemctl daemon-reload
sudo service gunicorn restart
```

gunicorn 상태확인

```bash
systemctl status gunicorn
```

