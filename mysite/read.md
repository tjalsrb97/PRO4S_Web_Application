#양준혁

#파이썬에서는 `mysqlclient`라는 라이브러리를 통해 MySQL과 DB를 연동할 수 있다.

```
$ pip install mysqlclient
```

DB 연결을 할 시 my_settings.py 를 이용하여 DATABASE를 가져와야함

```
import my_settings

DATABASES = my_settings.DATABASES
```
