## Web 이란?

- **웹 사이트**란 브라우저를 통해 접속하는 **웹 페이지**들의 모음
    - **웹 페이지**는 글, 그림, 영상 등의 정보를 담고 있으며, 다른 웹페이지로 이동하는 **링크**들이 있음.
    - **링크**로 여러 웹 페이지를 연결한 것을 **웹 사이트**라 함

- 웹 사이트 구성 요소
    - HTML : 구조(건물)
    - CSS : 표현(인테리어)
    - Javascript : 동작(엘리베이터)

- 웹 사이트는 브라우저를 통해 동작
- 브라우저 마다 동작이 달라서 문제가 생김(파편화)
- 웹 표준의 등장
    - 크롬, 엣지, 파이어폭스, 웨일 ...
- 웹 표준
    - 웹에서 표준적으로 사용되는 기술이나 규칙
    - 어떤 브라우저를 사용하든 웹 페이지가 동일하게 보이게 해줌


## HTML?
- Hyper Text Markup Language
    - Hyper Text
        - 하이퍼링크를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
    - Markup Language
        - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

- HTML style guide
    ```HTML
    <body>
      <h1> 웹문서 </h1>
      <ul>
        <li>HTML</li>
        <li>CSS</li>
      </ul>
    <body>
    ```

- HTML 기본 구조
    - 요소(element)
        - 시작 태그와 종료 태그, 그 사이에 내용으로 구성
            - 내용이 없는 태그도 존재
                - br, hr, img, input, link, meta
        - 요소는 중첩될 수 있음
            - 요소의 중첩을 통해 문서 구조화
            - 여는 태그와 닫는 태그의 쌍을 잘 확인해야 함
                - 오류 없이 깨진 상태로 반환

    - 속성(attribute)
        - \<a href="https://google.com"></a>
            - href : 속성 명
            - https~ : 속성 값
            - 공백 안됨, 쌍따옴표 사용
        - 태그의 부가적인 정보 설정
        - 경로나 크기 같은 추가적인 정보 제공
        - 보통 이름과 값이 하나의 쌍으로 존재함
        - 태그와 상관없이 사용 가능한 속성이 있음
            - id : 문서 전체에서 유일한 고유 식별자 지정
            - class : 공백으로 구분된 해당 요소의 클래스의 목록
            - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
            - style : inline 스타일
            - title : 요소에 대한 추가 정보 지정
            - tabindex : 요소의 탭 순서
    - 시맨틱 태그
        - 의미론적 마크업
    
    - html
        - 문서의 최상위 요소
    - head
        - 문서 메타데이터 요소
            - 문서 제목, 인코딩, 스타일, 외부 파일 로딩
            - 일반적으로 브라우저에 나타나지 않는 내용
        - \<title> : 브라우저 상단의 title
        - \<meta> : 문서 레벨 메타데이터 요소
        - \<link> : 외부 리소스 연결 요소
        - \<script> : 스크립트 요소
        - \<style> : CSS 직접 작성

    - body
        - \<!-- 이것은 주석 -->
        

    - form
        - \<form>은 정보를 서버에 제출하기 위해 사용하는 태그
        - action : form을 처리할 서버의 URL
        - method : form을 제출할 때 사용할 HTTP 메서드
        - enctype : method가 post인 경우 데이터의 유형
    - input
        - 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
        - name : form control에 적용되는 이름
        - value : form xontrol에 적용되는 값
        - required, readonly, autofocus autocomplete, disabled 등

    - input label