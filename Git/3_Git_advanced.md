# **undoing**
- commit 상태의 파일을 staging area로 내리는 것

- Working Directory 작업 단계
  - Working Directory에서 수정한 파일 냉ㅇ을 이전 커밋 상태로 되돌리기
  - git restore

- staging area 작업 단계
  - staging area에 반영된 파일을 working directory로 되돌리기
  - git rm --cached
  - git restore -- staged

- repository 작업 단계
  - 커밋을 완료한 파일을 staging area로 되돌리기
  - git commit --amend

**git restore**
  **working directory에서 수정한 파일을 수정 전으로 되돌리기**
  - 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
  - git restore를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의할 것!
  - git resotre {파일 이름}
  - git 2.23.0 이전 버전은 git checkout --{파일 이름}
  
  **Staging Area에 반영된 파일을 working derictory로 되돌리기**
  - root-commit 여부에 따라 두 가지 명령어로 나뉨
    - root-commit ?
      - 파일이 최초 생성 이후 한번의 커밋이 있었는지 없었는지
    - root-commit x : git rm --cached {파일 이름}
    - root-commit o : git restore --staged {파일 이름}

  **Repository 작업 단계 되돌리기**
  - git commit --amend
    - 커밋을 완료한 파일을 staging area로 되돌리기
    - 상황 별로 두 가지 기능으로 나뉨
      - staging area에 새로 올라온 내용이 없다면, 직전 커밋의 메시지만 수정
      - staging area에 새로 올라온 내용이 있다면, 직전 커밋을 덮어쓰기

**VIM**
- i : insert(끼워넣기) 모드
- esc : 끼워넣기 모드 탈출
- :wq : 저장하고 나가기



# **과거 버전으로 돌아가는 법**

### **git reset & revert**

- git reset
  - 현재 커밋에서 과거 커밋으로 돌아가는 것
  - 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
  - git reset [옵션] {커밋 ID}
    - 옵션은 soft, mixed, hard 중 하나(default: mixed)
    - 커밋 ID는 되돌아가고 싶은 시점의 커밋 ID를 작성(앞에 4자리 정도만 적어도 됨)

  - --soft
    - 해당 커밋으로 되돌아가고
    - 되돌아간 커밋 이후의 파일들은 staging area로 돌려놓음
  
  - --mixed
    - 해당 커밋으로 되돌아가고
    - 되돌아간 커밋 이후의 파일들은 working directory로 돌려놓음
    - git reset 옵션의 기본값
  
  - --hard
    - 해당 커밋으로 되돌아가고
    - 되돌아간 커밋 이후의 파일들은 모두 working directory에서 삭제!
    - 사용시 주의!
    - 기존의 Untracked 파일은 사라지지 않고 Untracked로 남아있음
    - git reflog
      - reset 하기 전의 과거 커밋 내역을 모두 조회 가능
      - 이후 해당 커밋으로 reset하면 복구 가능

- git revert
  - 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성
  - git revert {커밋 ID}
    - 커밋 ID는 취소하고 싶은 커밋 ID를 작성



# **branch**
- 브랜치는 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 도구
- 브랜치는 커밋을 가리키는 pointer

- 장점
  1. 브랜치는 독립 공간을 형성하기 떄문에 원본에 대해 안전함
  2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
  3. Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함
    - 변경 사항만 저장
    - 커밋들을 복사해서 저장하는 것이 아니라 특정 커밋을 가르키는 포인터를 생성

- 조회
  - git branch: 로컬 저장소의 브랜치 목록 확인
  - git branch -r: 원격 저장소의 브랜치 목록 확인

- 생성
  - git branch {브랜치 이름}: 새로운 브랜치 생성
  - git branch {브랜치 이름} {커밋 ID}: 특정 커밋 기준으로 브랜치 생성

- 삭제
  - git branch -d {브랜치 이름}: 병합된 브랜치만 삭제 가능
  - git branch -D {브랜치 이름}: 강제 삭제

- git switch
  - 현재 브랜치에서 다른 브랜치로 이동하는 명령어
  - git switch {브랜치 이름}: 다른 브랜치로 이동
  - git switch -c {브랜치 이름}: 브랜치를 새로 생성 및 이동
  - git switch -c {브랜치 이름} {커밋 ID}: 특정 커밋 기준으로 브랜치 생성 및 이동
  - switch하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋 해야함을 주의!
    - 다른 브랜치에서 파일을 만들고 커밋 하지 않은 상태에서 switch를 하면
      브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 됨

- git merge
  - 분기된 브랜치들을 하나로 합치는 명령어
  - master 브랜치가 상용이므로, 주로 master 브랜치에 병합
  - git merge {합칠 브랜치 이름}
    - 병합하기 전에 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야함
    - 병합에는 3종류 존재
      1. fast forward
        - 마치 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법

      2. 3 way merge
        - 각 브랜치 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법
      
      3. merge conflict
        - 충돌이 발생한 부분은 작성자가 직접 해결 해야함

- git push origin {브랜치 이름}
  - git push가 master 기준이기 때문에 해당 브랜치를 push하기 위해서는 위 명령어 사용

- head
  - head는 브랜치의 최신 커밋을 가리킨다고 볼 수 있다.
  - 특정 커밋으로 switch할 때만 헤드는 그 해당 커밋을 바라보고 브랜치에서 떨어져 나옴

- git checkout -t origin/{저장소명}
  - remote에 있는 branch 가져오기

- Public repo에 기여하기
  1. 기여하고자 하는 repo fork(내 repo로)
  2. local에 clone(내 repo)
  3. branch 생성
  4. branch에 작업
  5. git push origin {branch 이름}
  6. pullrequest 내 브랜치를 기여하고자 하는 repo mater branch로
  -> 상대가 수락하면 contributor에 등록 됨

### git workflow
https://techblog.woowahan.com/2553/
참고

### github-flow
  - 복잡한 git-flow를 개선하여 github에서 사용하는 방식
  - pull request 기능을 사용하도록 권장하며, 병합 후 배포가 자동화로 이루어짐

**브랜치를 자주 생서아는 것을 강력히 권장!**
**master브랜치 하나로만 작업하는 형태는 지양해야 함**