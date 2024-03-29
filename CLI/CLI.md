## CLI

**CLI ↔ GUI**

- **CLI(**Command Line interface)

  → 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식

- **GUI(**Graphic User interface)

  → 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식

- CLI 장점

  - 컴퓨터의 리소스 절약(GUI에 비해)
  - 수 많은 서버 / 개발 시스템이 CLI를 통한 조작 환경을 제공

### **CLI의 기본적인 명령어**

- **touch**

  - 파일을 생성하는 명령어

- **mkdir**

  - 새 폴더를 생성하는 명령어

- **ls**

  - 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어

- **cd**

  - 현재 작업 중인 디렉토리를 변경하는 명령어
  - cd .. → 부모 폴더로 이동(.. 은 부모 위치를 의미)

- **start/open**

  - 폴더/파일을 여는 명령어(Window → start, Mac → open)
  - start . ⇒ 현재 폴더 열어줌( . 은 현재 위치를 의미함)

- **rm**

  - 파일을 삭제하는 명령어
  - -r  옵션을 주면 폴더 삭제 가능
    - r 옵션은 recursion 으로 타고 타고 모두 삭제 하는 명령어

- **clear**

  - CLI창 모두 지우기
- **vi test.tst**
  - vi 편집기로 test.txt를 편집하겠다.
  - 명령모드(esc 눌렀을 때 혹은 vi 들어가자마자 상태)
    - i or insert: 현재 커서 위치에 삽입
![untitled](https://github.com/zzun-d/TIL/blob/master/CLI/CLI.assets/Untitled2.png?raw=true)

    - a: 현재 커서 바로 다음위치에 삽입
    - u: 방금 명령 취소
  <br>
  
  - 마지막 행 모드(esc 누르고 콜론(:) 누른상태)
    - w [파일명]: 파일 저장(꺼지지는 않음)
    - q: vi 종료(저장 안됨)
    - wq: 저장 후 종료
  <br>

  [이외의 vi 편집기 명령어 모음](https://blockdmask.tistory.com/25)

<br>

![untitled](https://github.com/zzun-d/TIL/blob/master/CLI/CLI.assets/Untitled.png?raw=true)  


~ ←표시가 현재 작업중인 위치(자주 써서 ~표시)

실제 ~ 주소는 **C:\Users\multicampus**

\~ 는 **Home directory**라고 함  

