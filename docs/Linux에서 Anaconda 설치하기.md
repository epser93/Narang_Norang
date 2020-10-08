# 리눅스에서 Anaconda 설치하기



## 0. 원하는 버전 선정

```
https://repo.anaconda.com/archive/
```



## 1. Conda 다운로드

```bash
sudo wget https://repo.anaconda.com/archive/[파일명]

ex)
sudo wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
```



## 2. Conda 설치하기

```bash
bash Anaconda3-2020.02-Linux-x86_64.sh
```

> 몇가지 동의해야할 것들이 나오는데 yes 처리해주면 됨
>
> 설치경로를 알려줄텐데 /home/[userid]/anaconda3 가 default임



## 3. path 설정

```bash
# 방법 1,2중 한가지로 하면 됨
vim ~/.bashrc # 방법1 vim 에디터 사용

gedit ~/.bashrc # 방법2 그냥 text Editor 사용
```

```vim
PATH = [경로]/bin:$PATH

ex)
PATH = /home/[userid]/anaconda3/bin:$PATH
```

> 경로에 conda를 설치할 때 알려준 경로를 집어넣어준다.



## 4. 변경내용 적용하기

```bash
source ~/.bashrc
```



## 5. conda 가상환경 적용되게 추가 setting 하기

```bash
source ~/anaconda3/etc/profile.d/conda.sh
```



## 6. 가상환경 활성화하기

```bash
conda activate 가상환경이름
```

