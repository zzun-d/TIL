# Data base
- 수 많은 데이터를 저장하는 공간
- 일반적으로 데이터는 파일에 저장
    - 성능, 보안적 측면에서 한계, 대용량 데이터 다루기 어려움, 구조적인 정리 어려움, 확장 불가능....
    - 다양한 단점이 존재

- 이후 등장한 스프레드 시트(엑셀)을 이용하여 데이터를 유형별로 구분하여 정리, 저장이 가능
- 데이터 베이스로 가는 단계로 스프레드 시트를 생각 가능

**RDB**
- 관계형 데이터베이스(Relational Database)
- 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
- 테이블간 관계 설정이 가능하여 여러 데이터를 쉽게 조작할 수 있는 장점이 있음
- SQL을 사용하여 데이터를 조회하고 조작
- **스키마**
    - 테이블 구조로 데이터베이스에서 자료 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것
-**테이블**
    - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
    - 관계라고도 부름
        - 필드: 속성, 컬럼
        - 레코드: 튜플, 행
    
**SQLite**
- 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 데이터베이스
- 오픈 소스 프로젝트로 자유롭게 사용 가능
- 대규모 동시 처리 작업에는 적합하지 않으며, 다른 RDMBS에서 지원하는 SQL 기능을 지원하지 않을 수 있음

---

## SQL Commands 종류

### 1. DDL(Data Definition Language)
- 데이터 정의 언어로 관계형 데이터베이스 구조를 정의하기 위한 명령어
- CREATE, DROP, ALTER


### 2. DML(Data Manipulation Language)
- 데이터 조작 언어로 데이터를 조작하기 위한 명령어
- INSERT, SELECT, UPDATE, DELETE


### 3. DCL(Data Control Language)
- 데이터 제어 언어로 데이터의 보안, 수행제어, 사용자 권한 부여 등을 정의 하기 위한 명령어
- GRANT, REVOKE, COMMIT, ROLLBACK
- 하지만, SQLite에는 권한 설정을 담당하는 GRANT, REVOKE를 지원하지 않아 생략

## SQL Syntax
- 모든 SQL 문은 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하며 하나의 문은 세미콜론으로 끝남
- SQL 키워드는 대소문자를 구분하지 않음(하지만 대문자로 작성하는 것을 권장)

### Statement & Clause

- Statement(문)
    - 독립적인 실행이 가능한 완전한 코드 조각
    - clause로 구성됨
- Clause(절)
    - statement의 하위 단위

```sql
SELECT column_name FROM table_name;
```
SELECT statement라 부르며
1. SELECT column_name
2. FROM table_name
두개의 clause로 구성


## DDL
- CREATE TABLE  
    - 데이터 베이스에 새 테이블을 만듦
    ```sql
    CREATE TABLE table_name (
        column_1 data_type constraints,
        column_2 data_type constraints
    );
    ```
    - data_type
        - NULL, INTEGER, REAL, TEXT, BLOB 등이 있음
        - NULL: 정보가 없거나 알 수 없음
        - INTEGER: 정수
        - REAL: 실수
        - TEXT: 문자 데이터
        - BLOB(Binary Large Object): 바이너리 등 멀티미디어 파일(주로 이미지 데이터)
    - SQLite는 동적 타입 시스템으로 컬럼에 저장된 값에 따라 데이터 타입이 결정됨

    - Constraints
        - NOT NULL: 컬럼이 NULL 값을 허용하지 않도록 지정
        - UNIQUE: 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
        - PRIMARY KEY: 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
        - AUTOINCREMENT: 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
    - rowid: 레코드의 고유 값으로 pk와 동일한 개념

- ALTER TABLE
    - 기존 테이블의 구조를 수정
    
    ```sql
    ALTER TABLE table_name RENAME TO new_table_name;

    ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;

    ALTER TABLE table_name ADD COLUMN column_definition;

    ALTER TABLE table_name DROP COLUMN column_name;
    ```
    - 맨 위부터 테이블 이름 변경, 컬럼명 변경, 새 컬럼 추가, 컬럼 삭제 명령어

- DROP TABLE
    - 데이터베이스에서 테이블을 제거
    - 한번에 하나의 테이블만 삭제 가능
    ```sql
    DROP TABLE table_name;
    ```


## DML

- 시작 전에 sqlite3 사용법

    - git bash에서 sqlite3 입력
    -> .open mydb.sqlite3 (자신의 db파일 이름 넣기)
    -> .exit(종료)

    - CSV 파일을 SQLite 테이블로 가져오기
    -> DML.sql 파일 생성
    -> 테이블 생성
    ```sql
    CREATE TABLE users (
        first_name TEXT NOT NULL,
        .
        .
        .
        balance INTEGER NOT NULL
    );
    ```
    -> git bash에서 sqlite3 mydb.sqlite3
    -> .mode csv
    -> .import users.csv users


- Simple query
    - SELECT 문을 사용하여 간단하게 단일 테이블에서 데이터 조회
    1. SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
    2. FROM 절에서 데이터를 가져올 테이블을 지정
    ```sql
    SELECT column1, column2 FROM table_name;
    ```
    - SELECT 문은 SQLite에서 가장 복잡한 문으로 다양한 명령어 존재
    - 모든 컬럼에 대한 약칭인 *을 사용 가능
    ```sql
    SELECT * FROM users;
    ```

- Sorting rows
    - ORDER BY절을 사용하여 쿼리 결과 정렬
    ```sql
    SELECT select_list FROM table_name
    ORDER BY column_1 ASC, column_2 DESC;
    ```
    - SELECT 문에 추가하여 결과를 정렬
    - 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC), 내림차순(DESC)로 정렬할 수 있음
    - NULL은 최솟값을 가짐

- Filtering data
    - 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기
    - Clause
        - SELECT DISTINCT: 조회 결과에서 중복된 행 제거
        ```sql
        SELECT DISTINCT slect_list FROM table_name;
        ```
        - WHERE
        - LIMIT
    - Operator: LIKE, IN, BETWEEN
