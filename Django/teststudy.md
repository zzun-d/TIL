frame work : 서비스 개발에 필요한 기능들을 미리 구현하여 모아 놓은 것
www : World Wide Web으로 전 세계에 퍼져 있는 거미줄 같은 연결망
웹서비스는 클라이언트 - 서버 구조를 기반으로 동작
클라이언트 -> requests -> 서버
클라이언트 <- responses <- 서버
웹 브라우저 : 웹에서 페이지를 찾아 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램 또는 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는(rendering) 프로그램
웹페이지
    - 정적 웹페이지 : 같은 상황에서 모든 사용자에게 동일한 정보 표시
        
    - 동적 웹페이지 : 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
디자인 패턴 : 자주 사용되는 구조가 있고, 그 것을 일반화 하여 하나의 공법으로 만든 것
디자인 패턴의 목적 : 공통된 문제 해결을 위한 재사용 가능한 해결책 제시

장고의 디자인 패턴 MTV
MVC에서 변형된 패턴으로
MVC는 각 model, view, controller를 뜻하며
    model : 데이터와 관련된 로직을 관리
    view : 레이아웃과 화면을 처리
    controller : 명령을 model과 view 부분으로 연결
MTV는 각 model, Template, View를 뜻함
    model : 데이터와 관련된 로직 관리, mvc 패턴에서 model에 해당, 응용프로그램의 데이터 구조를 정의하고 데이터 베이스의 기록을 관리

MTV 정리
m : 데이터 관련
t : 화면 관련
v : model & template 중간 처리 및 응답 반환
python -