## Git?

**→   분산 버전 관리 프로그램**

중앙 집중식 버전 관리 vs 분산 버전 관리

중앙 집중식 버전 관리 : 한 개의 중앙 서버에서 모든 데이터를 관리

분산 버전 관리 : 사용자 로컬 서버, 중앙 서버 모두에 서 데이터를 관리

분산 버전 관리의 장점 : 데이터를 분산 저장하여 하나의 서버가 터져도 다른 서버에 데이터가 남아있음

Git기반의 저장소 서버를 제공하는 서비스

→ **GitLab**, **Github**, **Bitbucket**

싸피에서 GitLab을 사용하는 이유?

→ GitLab은 서버를 사용자에게 직접 제공해줘서 기술 유출에 대한 위험이 없다.

→ 삼성 어딘가에 GitLab 서버가 있다.

<aside>
💡 Git ≠ GitHub
→ 분산 버전 관리 프로그램 그자체 ≠ Git 기반의 저장소 서비스

</aside>

- Github를 사용하면 좋은점
    - 공개적인 버전관리를 통해 성실함, 능력 어필 가능
    - 대표적인 협업 툴로 주니어 개발자에게 요구되는 팀 개발 능력 어필

이외의 협업툴로..

→ Slack, jira 등등

**Repository**

- 특정 디렉토리를 버전 관리하는 **저장소**
    - **git init** 명령어로 로컬 저장소를 생성
    - **.git** 디렉토리에 **버전 관리에 필요한 모든 것**이 들어있음
    
    ![Untitled](https://github.com/zzun-d/TIL/blob/master/Git/assets/Untitled.png?raw=true)
    
    - (master) ← git으로 관리됨을 뜻함

### Git 동작원리

- Working Directory ⇒ untracked 파일 생성
    
    **⇒ git add**
    
- Staging Area ⇒ staged(tracking)
    
    **⇒ git commit**
    
- Repository ⇒ committed(tracking)
    
    ⇒ **파일 수정**
    
- Working Directory ⇒ modified(tracked)

위 과정이 반복

### Git 기본기

- README.md 생성하기
    - 생성된 파일을 특정 버전으로 남긴다 ⇒ **커밋** 한다.
- 커밋은 3가지 영역을 바탕으로 동작
    - **Working Directory:** 내가 작업하고 있는 **실제 디렉토리**
    - **Staging Area:** **커밋**으로 남기고 싶은, **특정 버전**으로 관리하고 싶은 파일이 있는 곳
    - **Repository:** **커밋**들이 저장되는 곳(.git 폴더)
- **git status**
    - 현재 git으로 관리되고 있는 파일들의 상태를 알 수 있음
    
    ![Untitled](https://github.com/zzun-d/TIL/blob/master/Git/assets/Untitled%20(1).png?raw=true)
    

- **git commit -m**
    - 메세지와 함께 커밋
    
    ![Untitled](https://github.com/zzun-d/TIL/blob/master/Git/assets/Untitled%20(2).png?raw=true)
    

- **git log**
    - commit history 보기
    
    ![Untitled](https://github.com/zzun-d/TIL/blob/master/Git/assets/Untitled%20(3).png?raw=true)
    
    **→ commit 뒤에 오는 88eb104ca~~~~ 는 각 commit의 고유 아이디**
    

- **git diff A B**
    - A에 비해서 B가 어떻게 변했는지 나타냄
    - A, B는 각 commit의 고유 아이디(앞에 4자리 까지만 적어도 일반적으로 가능)
    
    ![Untitled](https://github.com/zzun-d/TIL/blob/master/Git/assets/Untitled%20(4).png?raw=true)
    <br>

- **git config --global user.name "~~~"**
- **git config --global user.email "~~~"**
    - global 옵션을 사용하면 해당 시스템에서 해당 사용자가 사용할 때는 이 정보를 사용함
    - 최초로 딱 한번만 시도하면 됨
<br>

- **git config --local user.name "~~~"**
- **git config --local user.email "~~~"**
    - global과 반대로 해당 폴더에서는 이 git name, email을 사용한다고 선언



**Github Repository** 생성

- **git remote add origin {remote_repo의 주소}**
    - origin : repo name(일반적으로 origin으로 이름을 사용)
- **git push A B**
    - A : push 할 위치(remote_repo)
    - B : 로컬 branch 위치(master)
    
    ![Untitled](https://github.com/zzun-d/TIL/blob/master/Git/assets/Untitled%20(5).png?raw=true)
    
    ![Untitled](https://github.com/zzun-d/TIL/blob/master/Git/assets/Untitled%20(6).png?raw=true)
    

- **git clone {remote_repo}**
    - remote repo를 local로 복사
    
    ![Untitled](https://github.com/zzun-d/TIL/blob/master/Git/assets/Untitled%20(7).png?raw=true)
    

- **git pull**
    - 연동된 github repo에 있는 내용을 복제해서 local에 저장한다.