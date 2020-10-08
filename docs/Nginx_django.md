# Nginx_django

## 1. nginx 설치

- 설치하지 않았다면 nginx를 설치해야 한다.

```bash
sudo apt-get install nginx
```





## 1. nginx 설정

```bash
sudo vim /etc/nginx/site-enabled/default
```




```python
upstream backend {
    	# server 서버주소	
    	server localhost:8000;
    	# 여러개 등록이 가능하다.
    	# 여러개 등록시 라운드로빈으로 분배된다.
}


server {
    	...
    	# 기타내용 중략
    
		# 서버와 연결해주는 코드
        location / {
                proxy_pass http://backend;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
        }
		# 서버의 static 파일들과 연결해주는 코드
    	# 설정해주지 않는다면 static과 연관된 기능들이 동작하지 않는다. ex)css
        location /static/ {
            	# static 폴더가 있는 경로를 적어준다.
                root /home/ubuntu/project/s03p23c206/backend;
        }
		# 서버의 데이터파일들을 연결해주는 코드
    	# 사진 동영상, 음악파일 등
        location /media {
                alias /home/ubuntu/project/s03p23c206/backend/media;
        }
}

```

