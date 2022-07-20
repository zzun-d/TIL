# 0. Python 기초
----

### 기초 문법

#### 변수(Variable)
- 데이터를 저장하기 위해서 사용
- 복잡한 값들을 쉽게 사용할 수 있음(**추상화**)
- 동일한 변수에 다른 데이터를 언제나 저장할 수 있기 때문에, '변수'라고 불림

**추상화**
- 변수를 사용해야 하는 이유
- 일일이 값을 넣는 것도 불편, 오타 위험, 다른 사람이 코드를 알아보기 힘듬 등등
ex)
```python
print(2000)
print(2000 + 2000)
print(3000 * 2 + 3500 * 3 + 4000 + 5)
```
```python
americano_price = 2000
mocha_price = 3000
cookie_price = 2000
cake_price = 4000
lemonade_price = 3500

print(americano_price)
print(americano_price + cookie_price)
print(mocha_price * 2 + lemonade_price * 3 + cake_price * 5)
```
- 같은 코드여도 가독성이 다르다!
- 숫자를 적지 않고, 의미 단위로 작성 가능
- 코드 수정이 용이해짐 - 아메리카노 가격이 변경되더라도 한 곳만 수정하면 됨
<br>


**변수의 할당**
- 변수는 '='를 통해 값을 할당
`dust = 1`
- 같은 값을 동시에 할당 가능
`dust = trash = 1`
- 다른 값을 동시에 할당 가능
`dust, can = 1, 2`

<br>

**각 변수의 값 바꿔서 저장하기**
- 임시 변수 활용(일반적인 경우)
```python
x, y = 10, 20
tmp = x
x = y
y = tmp
print(x, y) # 20, 10
```
- Pythonic!
```python
x, y = 10, 20
y, x = x, y
print(x, y) # 20 10
```
<br>

**식별자**(이름)
- 변수 이름 규칙
    - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
    - 첫 글자에 숫자가 올 수 없다
    - 길이 제한이 없고, 대소문자를 구별한다
    - 예약어는 변수 이름으로 사용할 수 없다
    ```python
    import keyword
    print(keyword.kwlist)

    # 출력 결과
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
     'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
     'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
     'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
     'while', 'with', 'yield']
    ```
    - 다른 곳에서 쓰는 이름도 사용하면 안됨(내장 함수, 모듈 등)

<br>

----

#### 연산자

- 산술 연산자(Arithmetic Operator)
    - 기본적인 사칙연산 및 수식 계산
    - +, -, *, / : 일반적인 사칙연산
    - //, %, ** : 몫, 나머지, 지수

- 논리 연산자
    - 참 거짓을 판명
    - 아래서 자세하게 나타냄

<br>

----

#### 자료형(Datatype) 분류

- 프로그래밍에서는 다양한 종류의 값을 쓸 수 있음
    - 사용할 수 있는 데이터의 정류를 자료형(Datatype)이라고 함
    - Boolean Type: 참/거짓
    - Numeric Type: 숫자(int, float, complex:복소수)
    - String Type: 문자열
    - None

<br>

- **정수 자료형(int)**
    - 0, 100, -10과 같은 정수를 표현하는 자료형
    - 일반적인 수학 연산 가능

<br>

- **진수 표현**
    - 2진수(binary): 0b
    - 8진수(octal): 0o
    - 16진수(hexadecimal): 0x
    ```python
    print(0b10) # 2
    print(0o30) # 24
    print(0x10) # 16
    ```

<br>

- **실수 자료형(float)**
    - 0.001, 10.0 등과 같은 유리수와 무리수를 표현하는 자료형
    - **실수 연산시 주의할 점(부동 소수점)**
        - 실수의 값을 처리할 때 의도하지 않은 값이 나올 수 있음
        ```python
        print(3.2 - 3.1) # 0.10000000000000009
        print(1.2 - 1.1) # 0.09999999999999987
        ```
        값이 다름!

        <br>

    - 해결책
        - 값 비교하는 과정에서 정수가 아닌 실수면 주의!
        - 매우 작은 수보다 작은지를 확인하거나 math 모듈 활용
        ```python
        a = 3.2 - 3.1 # 0.10000000000000009
        b = 1.2 - 1.1 # 0.09999999999999987

        #1. epsilon 사용
        print(abs(a - b) <= 1e-10) # True

        # 2. python 3.5이상에서
        import math
        print(math.isclose(a, b)) # True
        ```
        <br>

- **문자열 자료형**
    - 모든 문자는 str 타입
    - 작은따옴표(')나 큰따옴표(")를 활용하여 표기
        - 문자열을 묶을 때, 동일한 문장푸호를 활용
        - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함
        (처음에 (')를 사용했으면 이후에도 (')만 사용)

    <br>

    - **중첩 따옴표**
        - 작은 따옴표가 들어 있는 경우 큰따옴표로 문자열 생성(반대도 가능)
        ```python
        print("문자열 안에 '작은따옴표'를 사용하면 큰 따옴표로 묶음")
        
        # 문자열 안에 '작은따옴표'를 사용하면 큰 따옴표로 묶음
        ```

    <br>

    - **삼중 따옴표**
        - 따옴표 안에 따옴표를 넣을 때, 여러줄을 나눠 입력할 때 편리
        ```python
        print('''문자열 안에 '작은따옴표'와 "큰따옴표"를 
        함께 사용가능하고,
        여러 줄을 사용할 때도 편리''')

        # 문자열 안에 '작은따옴표'와 "큰따옴표"를
        함께 사용가능하고,
        여러 줄을 사용할 때도 편리
        ```
    <br>

    - **Escape sequence**
        - 역슬래시 뒤에 특정 문자를 써서 특수한 기능을 하는 문자 조합
        - \n: 줄바꿈
        - \t: 탭
        - \r: 캐리지 리턴
        - \O: 널(Null)
        - \\\\: \
        - \\': 단일인용부호(')
        - \\": 이중인용부호(")  

    <br>

    - **문자열 연산**
        - 덧셈
            - 문자열을 연결
            `print("Hello" + "World") # HelloWorld`
        - 곱셈
            - 문자열을 여러번 반복
            `print("Python" * 3) # PythonPythonPython`

    <br>

    - **String Interpolation(문자열을 변수를 활용하여 만드는 법)**
        - %-formatting
        ```python
        name = 'Lee'
        score = 3.4

        print('Hello, %s' % name) # Hello, Lee
        print('내 성적은 %d' % score) # 내 성적은 3
        print('내 성적은 %f' % score) # 내 성적은 3.400000
        ```

        - str.format()
        ```python
        name = 'Lee'
        score = 3.4

        print('Hello, {}! 성적은 {}'.format(name, score))
        # Hello, Lee! 성적은 3.4
        ```

        - f-strings
        ```python
        name = 'Lee'
        score = 3.4

        print(f'Hello, {name}! 성적은 {score}')
        # Hello, Lee! 성적은 3.4
        ```

        <br>

- **None**
    - 파이썬 자료형 중 하나로 값이 없음을 표현
    - 일반적으로 반환 값이 없는 함수에서도 사용

<br>

- **불린형(Boolean)**
    - 논리 자료형으로 참과 거짓을 표현하는 자료형
    - True, False를 값으로 가짐
    - 비교나 논리 연산에서 사용

    <br>

    - **비교 연산자**
        - <: 미만
        - <=: 이하
        - \>: 초과
        - \>=: 이상
        - ==: 같음
        - !=: 같지 않음
        - is: 객체 아이덴티티
        - is not: 객체 아이덴티티가 아닌 경우

    <br>

    - **논리 연산자**
        - 여러 가지 조건이 있을 때
            - 모든 조건을 만족(and), 여러 조건 중 하나만 만족해도 됨(or)
        - 일반적으로 비교 연산자와 함께 사용
        - A and B: A와 B 모두 True시, True
        - A or B: A와 B 모두 Fasle시, False
        - Not: True를 False로, False를 True로

        ```python
        num = 10
        print(num >= 100 and num % 3 == 1) # True
        print(True and False) # False
        print(True or False) # True
        ```
        
        <br>

        - **논리 연산자 주의할 점 / not 연산자**
            - Falsy: False는 아니지만 False로 취급 되는 다양한 값

                - 0, 0.0, (), [], {}, None, ""(빈 문자열)
            - 논리 연산자도 우선순위가 존재함
                - not, and, or 순으로 우선순위 높음

            ```python
            print(not True) # False
            print(not 0) # True
            print(not 'hi') False
            print(not True and False or not False) # True
            #위 코드와 같은 코드
            print(((not True) and False) or (not False)) # True
            ```

        <br>

        - **논리 연산자 단축 평가**
            - 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환
            - and 연산에서 첫번째 값이 False인 경우 무조건 False
            - or 연산에서 첫번째 값이 True인 경우 무조건 True
            ```python
            print(5 and 4) # 4
            print(5 or 3) # 5
            print(0 and 5) # 0
            print(5 or 0) # 5
            ```

            <br>

----
#### 컨테이너
- 여러 개의 값을 담을 수 있는 객체, 서로 다른 자료형을 저장할 수 있음
    - list, dict, set, tuple
- 컨테이너의 분류
    - 순서가 있는 데이터(Ordered) vs. 순서가 없는 데이터(Unordered)
    - 순서가 있다고 정렬되어 있다는 뜻은 아님! 
        
    <br>

    - **컨테이너**
        - sequence(ordered) 형
            - list
            - tuple
            - range
        - nonsequence(unordered) 형
            - set
            - dictionary

<br>

- **sequence 형**

<br>

- **list**
    - list는 대괄호([]) 혹은 list()를 통해 생성 가능
        - 파이썬에서는 리스트 안에 어떠한 자료형도 저장이 가능(리스트 안에 리스트도 가능)
        - 생성된 이후 내용 변경 가능(가변 자료형)
        - 이런 유연성 때문에 파이썬에서 가장 흔하게 사용
    - sequence 데이터로 인덱스를 이용하여 접근 가능
        - list[i]
        ```python
        list_a = [1, 2, '삼', '사']
        print(list[0]) # 1
        print(list[2]) # '삼'
        ```

<br>

- **tuple**
    - tuple은 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
        - 리스트와의 차이점은 생성 후, 담고 있는 값의 수정이 불가(불변 자료형)
    - 항상 소괄호 형태로 사용 

    <br>

    - **tuple 생성 주의사항**
        - 단일 항목의 경우에 값 뒤에 쉼표를 붙여야 함
        `tuple_a = (1,)`
        - 복수 항목의 경우에도 넣는 것을 권장(Trailing comma)
        `tuple_b = (1, 2, 3,)`
    - **tuple 대입**
        - 우변의 값을 좌변의 변수에 한 번에 할당하는 과정
        ```python
        x, y = 1, 2
        print(x, y) # 1 2

        # 실제로 tuple로 처리
        x, y = (1, 2)
        print(x, y) # 1 2

<br>

- **Range**
    - 숫자의 sequence를 나타내기 위해 사용
    - 주로 for 반복문과 함께 사용

    <br>

    - **Range 사용 방법**
        - 기본형: range(n)
            - 0부터 n-1까지의 숫자 sequence
        - 범위 지정: range(n, m)
            - n부터 m-1까지의 숫자 sequence
        - 범위 및 스텝 지정: range(n, m, s)
            - n부터 m-1까지 s만큼 증가시키며 숫자의 sequence

<br>

- **슬라이싱 연산자**
    - 인덱스와 콜론을 사용하여 문자열의 특정 부분만 잘라낼 수 있음
    - 슬라이싱을 사용할 때 콜론을 기준으로 앞 인덱스는 포함, 뒤 인덱스는 미포함
    ```python
    print([1, 2, 3, 5][1:4]) # [2, 3, 5]
    print('abcd'[2:4]) # 'cd'
    ```

    <br>

    - **sequence를 k 간격으로 슬라이싱**
    ```python
    print([1, 2, 3, 5][0:4:2]) # [1, 3]
    print(range(10)[1:5:3]) # range(1, 5, 3)
    ```

<br>

**nonsequnece**

<br>

- **set**
    - 중복되는 요소 없고, 순서 상관없는 데이터들의 묶음
        - 중복을 허용하지 않기 때문에 중복되는 원소는 하나만 저장
        - 순서가 없기 때문에 인덱스를 이용한 접근 불가
    - 수학에서의 집합을 표현한 컨테이너
        - 집합 연산이 가능(여집합은 별도로 존재하지 않음)
    - 담고 있는 요소를 삽입, 변경, 삭제 가능(가변 자료형)

    - 중괄호({}) 혹은 set()을 통해 생성
        - 빈 set을 만들기 위해서는 반드시 set()을 사용
    
    <br>

    - **set 사용꿀팁**
        - set은 중복되는 값을 지울 때, 많이 사용
        - 하지만, 순서가 중요한 데이터에는 사용하면 안됨!
    - **set 연산자**
        - |: 합집합
        - &: 교집합
        - -: 차집합
        - ^: 대칭차집합(합집합 - 교집합)
        ```python
        set_a = {1, 2, 3, 4}
        set_b = {1, 2, 3, "Hello", (1, 2, 3)}

        print(set_a | set_b) # {1, 2, 3, 4, (1, 2, 3), 'Hello'}
        print(set_a & set_b) # {1, 2, 3}
        print(set_a - set_b) # {(1, 2, 3), 'Hello'}
        print(set_a ^ set_b) # {4, (1, 2, 3), 'Hello'}
        ```

<br>

- **dictionary**
    - 키-값(key-value) 쌍으로 이뤄진 자료형(3.7 부터는 ordered, 이하 버전 unordered)
    - key는 변경 불가능한 데이터만 활용 가능
        - string, integer, float, boolean, tuple, range
    - value는 어떠한 형태든 관계 없음
    
    <br>

    - **dictionary 생성**
        - 중괄호({}) 혹은 dict()을 통해 생성
        - key를 통해 value에 접근
        ```python
        dict_a = {1 : 'one', 2 : 'two', 'list' : [1, 2]}
        print(dict_a[1]) # 'one'
        print(dict_a['list']) # [1, 2]

        dict_b = dict(a='apple', b='banana', lst=[1, 2, 3])
        print(dict_b) # {'a' : 'apple, 'b' : 'banana', 'lst' : [1, 2, 3]}
        ```
    
    <br>

----
#### 형변환
- 파이썬에서 데이터 형태는 서로 변환 가능
- **암시적 형 변환(Implicit)**
    - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환
    - bool, Numeric type(int, float)
    - 암시적 형 변환은 지양하고, 반드시 명시적 형 변환으로 사용
    ```python
    print(True + 3) # 4
    print(3 + 5.0) # 8.0
    ```

- **명시적 형 변환(Explicit)**
    - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환

    <br>

    - **int**
        - str, float → int
        - 단, 형식에 맞는 문자열만 정수로 변환

        ```python
        print('3' + 4) # TypeError
        
        # 명시적 타입 변환 필요
        print(int('3') + 4) # 7

        # float 형식의 string은 변환 불가
        print(int(3.5) + 4) # ValueError
        ```
        
    - **float**
        - str(참고), int → float
        - 단, 형식에 맞는 문자열만 정수로 변환

        ```python
        print('3.5' + 3.5) TypeError

        # 정수 형식인 경우에도 float으로 타입 변환
        print(float('3')) # 3.0

        # float 형식이 아닌 경우 타입 변환 불가
        print(float('3/4') + 5.3) # ValueError
        ```

    - **str**
        - int, float, list, tuple, dict → str
        ```python
        print(str(1)) # 1
        print(str(1.0)) # 1.0
        print(str([1, 2, 3])) # [1, 2, 3]
        ```
        
<br>



