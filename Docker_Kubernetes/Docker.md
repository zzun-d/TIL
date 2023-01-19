# Docker

---

## Docker를 들어가기 전에..

### DevOps?

- 소프트웨어 개발(Development) + 운영(Operations)
- 조직이 소프트웨어 제품과 서비스를 빠른 시간에 개발 및 배포하는 것을 목적으로 함
- 개발 프로세스의 변화
  - 코드 작성 -> 클라우드
  - 코드작성 -> Git -> CI -> CD -> 클라우드 -> 모니터링
- 개발과 배포는 복잡하다 !
- 위 복잡한 과정을 DepOps를 사용하면 조금 쉽고 빠르게 가능
- 결론적으로 DevOps란, 철학이면서 방법론이며 문화이다.
  - 좋은 도구를 잘 사용해서 자동화, 측정, 공유, 축적 !
  - 현재 사람들이 많이 사용하는 좋은 도구 예
    - git, docker, kubernetes ...
- 우리 조직에 DevOps를 도입하면 일률이 향상될 것인지 생각을 해봐야 함
- 새로운 기술을 배우는 이유는 개발과 배포의 개선
- 새로운 도구를 도입한 이후에 개발, 배포가 개선되지 않으면 재검토가 필요

<br>
### 자체 서버 운영
- 서버 주문 > 서버설치 > CPU, 메모리, 하드디스크 조립 > 네트워크 연결 > OS 설치 > 계정 설정 > 방화벽 설정 ...
- 매우 복잡
- 배포 역시 매우 복잡
- 버젼 변경도 복잡

- 서버 관리 해결 시도

  1. PPT로 서버 관리법을 상세하게 기술하여 공유
     - 문서의 정확성, 공유 문제, 운영체제의 변화에 적용 어려움 등의 문제가 있음
  2. 상태관리 도구
     - CHEF, puppet, ANSIBLE...
     - 설정파일로 관리
     - 문서보다 코드로 관리하기 때문에 쉬워지고 버전관리도 가능
     - 하지만 사용이 어렵고 러닝커브가 존재, 한 서버에 여러 버전설치 불가
  3. 가상머신

     - Jenkins, Wordpress, Chat...
     - 한 서버에 여러개 설치 쉽다
     - 현 상태 저장도 가능
     - 하지만 처음부터 다시 셋팅이 어렵움, 서버가 느림, 이미지 공유가 어려움

  4. 클라우드

     - AWS, Google Cloud, Azure ...
     - 가상화된 아키텍처 구성이 가능
     - 이미지를 기반으로 다수의 서버 상태 관리
     - 전기 사용하듯 편리

  5. PaaS
     - Vercel, Heroku, Netlify, AWS Elastic Beanstalk, Google Cloud App Engine ...
     - 잘 구성해 놓은 곳에 소스 코드만으로 배포(엄청 빠름)
     - 일반화된 프로비저닝 방법을 제공
     - 애플리케이션을 PaaS 방식에 맞게 작성해야 함
     - 서버에 대한 원격 접속 시스템 제공 X
     - 서버에 파일 시스템 사용 불가
     - 서버 패키지 설치 불가
     - 로그 수집 제한
       > **PaaS에서 가능한 일들 ?**
       > 크론잡(문자 발송, 예약, 정산 등)
       > 데이터 분석
       > 로그 분석
       > 애플리케이션 성능 모니터링
       > A/B 테스트, Canary 배포
       > 네트워크, 스토리지 설정

<br>

## Docker와 Kubernetes의 등장

### Docker

- 도커의 등장으로 서버관리가 편해짐
- 프로그램마다 컨테이너로 관리하여 단순한 명령어 한줄로 프로그램을 서버에서 실행이 가능함
- 어떤 플랫폼에서든 돌아감(AWS, Azure, Google Cloud, ucloud biz ...)
- 가상머신의 차이점
  - 가상머신처럼 독립적인 실행이 가능하지만,
  - 더 빠르고, 더 쉽고, 더 효율적 !
- 핵심 기능은 **자원 격리**
  - 프로세스, 파일, 디렉토리를 가상으로 분리
  - CPU, MEMORY, I/O 그룹별로 제한
- 리눅스 기능을 이용하여 효과적인 서버 관리

> **도커 이용 요약**
> 코드작성 -> 빌드(도커 이미지 생성) -> 이미지 다운 -> 도커에서 실행 !
> 도커 이미지: 압축파일로 생각하면 됨
> <br>

#### Container Orchestration

- 프로비저닝 및 배포
- 구성 및 일정 조정
- 리소스 할당
- 컨테이너 가용성nbsp;
- 인프라 전반의 워크로드 밸런싱을 기반으로 컨테이너 스케일링 또는 제거
- 로드 밸런싱 및 트래픽 라우팅
- 컨테이너 상태 모니터링
- 실행될 컨테이너를 기반으로 애플리케이션 설정
- 컨테이너 간 상호 작용의 보안 유지

### Kubernetes

- 컨테이너 오케스트레이션
- 오픈소스, 인기 多, 확장성(머신러닝, CI/CD 등), 사실상의 표준
- 공부가 필요..!