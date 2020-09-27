# Nginx 

## 1. nginx 설치하기

```bash
sudo apt-get install nginx
```



## 2. nginx 설정하기

```bash
sudo vim /etc/nginx/site-enabled/default
```



```python
#root /var/www/html;
#root 화면에보여질파일경로 설정하기
#예를들어서 vue.js 라고한다면 build후 생긴 dist 폴더를 경로로 설정
root /home/ubuntu/project/dist;
```



## 3. SPA일때 새로고침, url이동이 안될때

```python
    	location / {
                # try_files $uri $uri/ =404;
                #url로 이동하는것을 허용하는 코드
                try_files $uri $uri/ /index.html;
        }
```



## 4. 설정이 끝났다면 nginx 재시작하기

```bash
sudo service nginx restart
```

