# nginx


```python
        #front 파일
    	root /home/ubuntu/project/s03p23c206/frontend/dist;

    
    	location / {
                # try_files $uri $uri/ =404;
                #url로 이동하는것을 허용하는 코드
                try_files $uri $uri/ /index.html;
        }
		# 서버와 연결해주는 코드
        location /api {
                proxy_pass http://backend;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
        }
		# 서버의 static 파일들과 연결해주는 코드
        location /static/ {
            	# static 폴더가 있는 경로를 적어준다.
                root /home/ubuntu/project/s03p23c206/backend;
        }
		# 서버의 데이터파일들을 연결해주는 코드
        location /media {
                alias /home/ubuntu/project/s03p23c206/backend/media;
        }
```

