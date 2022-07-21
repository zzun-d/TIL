# 3. Python 모듈
---

## 1. 모듈과 패키지
- **module**
    - 합, 평균, 표준편차 등등 자주 쓰는 기능들을 하나의 파일(.py)로 옮긴 것
    - [파이썬에 기본적으로 설치된 모듈과 내장 함수](https://docs.python.org/ko/3/library/index.html)

- **package**
    - 특정 기능과 관련된 여러 모듈의 집합으로, package 안에는 또 다른 sub package를 포함

    - **가상환경** : package의 활용 공간
        - 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우
        - 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
        - 이런 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음
        - 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
        - bash에서의 **가상환경 활성화/비활성화**
            - 활성화 : $ source \<venv>/bin/activate
            - 비활성화 : $ deactivate
            

           
   

            



    <br>


    - **pip** 
        - PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
        - **설치**
            - **$ pip install SomePackage**
            - **$ pip install SomePackage==1.0.5**
            - **$ pip install 'SomePackage>=1.0.4**
        - 삭제
            - $ pip uninstall SomePackage
        - 목록
            - $ pip list
        - 패키지 정보
            - $ pip show SomePackage
        - **패키지 박제(내가 설치한 패키지들)**
            - **$ pip freeze > requirements.txt**
        - **박제된 패키지 목록 설치**
            - **$ pip install -r requirments.txt**
        
        <br>

    - **패키지는 여러 모듈/하위 패키지로 구조화**
    - **모든 폴더에는 \_\_init\_\_.py를 만들어 패키지로 인식**
        - python 3.3부터는 파일이 없어도 되지만, 하위 버전 호환을 위해 생성을 권장
<br>

- **libarary**
    - 다양한 패키지를 하나의 묶은 도구

<br>
 
- **모듈과 패키지 불러오기**
    - **import module**
    - **from module import var, function, class**
    - **from module import \***
    - **from package import module**
    - **from package.module import var, function, class**




