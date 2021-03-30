#양준혁

#파이썬에서는 `mysqlclient`라는 라이브러리를 통해 MySQL과 DB를 연동할 수 있다.

```
$ pip install mysqlclient
```

DB 연결을 할 시 my_settings.py 를 이용하여 DATABASE를 가져와야함

my_settings.py 내용을 적절히 수정바람(Host, 비밀번호 )

```
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'webdb',  
        'USER': 'root',  
        'PASSWORD': 'password',  
        'HOST': 'DBIPADDRESS',   
        'PORT': '3306',  
    }
}

```
settings.py DATABASE를 하단과 같이 변경

```
import my_settings

DATABASES = my_settings.DATABASES
```
