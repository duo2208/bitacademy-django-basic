# DJango 초기설정

## ver-VSCode
### 1. 가상환경 만들기 
'''
python -m venv 가상환경이름
'''

### 2. 가상환경 켜기
'''
source 가상환경이름/Scripts/acitvate
'''

### 3. 가상환경에 장고 설치하기
'''
 pip install django
 '''
### 3-1. 가상환경에 mysqlclient 설치하기
'''
pip install mysqlclient
'''

### 4. 장고 프로젝트 만들기
'''
django-admin startproject 프로젝트 이름
'''

### 5. 디렉토리 정리
vscode의 프로젝트와 장고 프로젝트를 일치시켜주기
### 5-1. 서버 구동 확인
'''
python manage.py runserver
'''

### 6. 초기 설정 : settings.py 에서 
    (1) time zone 설정 : TIME_ZONE = 'Asia/Seoul'
    (2) database 설정 : DATABASES = {
                        'default': {
                            'ENGINE': 'django.db.backends.mysql',
                            'NAME': 'webdb',
                            'USER': 'webdb',
                            'PASSWORD': 'webdb',
                            'HOST': 'localhost',
                            'PORT': 3306
                        }
                    }

### 7. 장고 프로젝트의 관리 어플리케이션(기본설치)이 사용하는 DB 생성
'''
 python manage.py migrate
'''

'''
* 호환문제 : (manage.py) 
from django.db.backends.mysql.base import DatabaseWrapper 
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
'''

### 8. 프로젝트 관리자 계정 만들기
'''
python manage.py createsuperuser
'''

### 9. 프로젝트 안에 앱 만들기
'''
python manage.py startapp 앱이름
'''

### 10. 프로젝트에 앱 만든거 알리기: settings.py에 
INSTALLED_APPS = 
    ‘앱이름.apps.앱이름 대문자로 시작Config’,

