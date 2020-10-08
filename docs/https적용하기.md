

# https 적용하기

## 1. apt 최신화 

```bash
sudo apt-get update
sudo apt-get install software-properties-common
```



## 2. certbot 설치(무료 ssh발급)

```bash
sudo apt-get install certbot python3-certbot-nginx
```



## 3. certbot을 이용하여 https적용

```bash
sudo certbot --nginx -d example.com
```

- 설정시 2번(리다이렉트 적용) -> nginx에서 자동으로 리다이렉트 시킴



## 출처 

https://twpower.github.io/44-set-free-https-by-using-letsencrypt

