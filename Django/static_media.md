# static files
## 정적 파일
- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
- 파일 자체가 고정, 변경 없음
- 이미지, 자바 스크립트, CSS 등이 정적 파일

### Media file
- 사용자가 웹에서 업로드하는 정적 파일


## static files 구성
1. INSTALLED_APPS에 django.contrib.staticfiles가 포함되어 있는지 확인
2. settings.py에서 STATIC_URL 확인
3. 앱의 static 폴더에 정적 파일을 위치하기
    - ex) my_app/static/sample_img.jpg
4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

### Django template tag
- **load**
    - 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
    - import와 같은 태그라 생각하면 됨

- **static**
    - STATIC_ROOT에 저장된 정적 파일에 연결

### static files 관련 Core settings
1. **STATIC_ROOT**
    - Default: None
    - collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
    - 개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음
    - 실 서비스 환경에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위해 사용
    - 배포 환경에서는 django를 직접 실행하는 것이 아니라, 다른 서버에 의해 실행되기 때문에 실행하는 다른 서버는 django에 내장된 정적 파일들을 인식하지 못함

2. **STATICFILES_DIR**
    - Default: [](empty list)
    - app/static/ 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
    - 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함


3. **STATIC_URL**
    - Default: None
    - STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL
    - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색
    - 실제 파일이나 디렉토리가 아니며, URL로만 존재
    - 비어 있지 않은 값으로 설정 한다면 반드시 / 로 끝나야 함

### static file 가져오기
1. 기본 경로에 있는 static files 가져오기
    1. articles/static/articles 경로에 이미지 파일 배치하기
    2. static tag를 사용해 이미지 파일 출력하기

2. 추가 경로에 있는 static files 가져오기
    1. 추가 경로 작성
        ```python
        STATICFILES_DIRS = [
            BASE_DIR / 'static',
        ]
        ```
    2. static/경로에 이미지 파일 배치
    3. 마찬가지로 static tag를 이용해 이미지 파일 출력

### ImageField()
- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능
- 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
- ImageField 인스턴스는 최대 길이가 100자인 문자욜로 DB에 생성, max_length 인자를 사용 가능

### FileField()
- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자를 갖고 있음
    1. upload_to
    2. storage

### FileField/ImageField를 사용하기 위한 단계
1. settings.py에 MEDIA_ROOT, MERIA_URL 설정
2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정

### MEDIA_ROOT
- Default: ''(empty string)
- 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로
- 장고는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않고 **파일 경로**만 저장함
- MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함

### MEDIA_URL
- Default: ''(empty string)
- MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
- 업로드 된 파일의 주소를 만들어 주는 역할
    - 웹 서버 사용자가 사용하는 public URL
- 비어있지 않은 값이라면 /로 끝나야함
- MIDEA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야 함


MEDIA 파일은 따로 추가되기 때문에, urls.py에 url에 추가가 필요함


    ```python
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [

    ] + static(settings.MEDIA.URL, document_root=settings.MEDIA_ROOT)
    ```

### Create
- ImageField 작성
    ```python
    # articles/models.py

    class Article(models.Model):
        image = models.ImageField(black=True)
    ```
- Model field option
    1. blank
        - Default: False
        - True인 경우 필드를 비워 둘 수 있음, 이 경우 DB에는 ''이 저장 됨
        - 유효성 검사에서 사용 됨
    
    2. null
        - Default: False
        - True인 경우 django는 빈 값을 DB에 NULL로 저장
        **null 관련 주의사항**
        - CharField, TextField와 같은 문자열 기반 필드에는 null 옵션 사용을 피해야 함
            - 문자열 기반 필드에 null=True로 설정 시 데이터 없음에 대한 표현에 빈 문자열과 null 모두 가능하게 됨
            - 데이터 없음에 대한 표현에 두 개 의 가능한 값을 갖는 것은 좋지 않음

- Migrations
    - ImageField를 사용하려면 반드시 Pillow 라이브러리 필요
    - Pillow: 광범위한 파일 형식을 지원하며 효율적이고 강력한 이미지 처리 기능

- ArticleForm에서 image 필드 출력 확인
    - 이미지가 업로드 되지 않음
    - create.html의 form 태기에 enctype 속성을 변경해야함
        '''html
        <form action="{%url 'articles:create' %}" method="POST" enctype="multipart/form-data">
        '''

- request.FILES
    - 파일 및 이미지는 request의 POST 속성 값으로 넘어가지 않고 FILES 속성 값에 담김
    - view.create 함수 변경
    ```python
    def create(request):
        if request.method == 'POST':
            from = ArticleForm(request.POST, request.FILES)
    # request.FILES는 두번째 인자
    ```

- 이미지를 첨하지 않으면 blank=True 속성으로 인해 빈 문자열 저장
- 이미지 첨부시 MEDIA_ROOT 경로에 이미지 업로드
- 같은 이름의 이미지 업로드시 이름 끝에 임의의 난수를 붙여 저장

### READ
- 업로드 된 파일의 상대 url은 django가 제공하는 url 속성을 통해 얻을 수 있음
- img 태그를 이용
    - src="{{ article.image.url }}" alt="{{ article.image }}"


### UPDATE
- update.html 파일에 enctype값 create와 동일하게 multipart/form-data로 추가
- create view 함수와 마찬가지로 update view 함수에 
    form = ArticleForm(request.POST, request.FILES, instance=article)

