# 2. Python 제어문 및 함수
----
## 1. 제어문
- 파이썬은 위에서 아래로 차례대로 명령을 수행
- 특정 상황에 따라서 코드를 선택적으로 실행 하거나 계속해서 실행하는 제어가 필요
- 제어문은 순서도로 표현 가능

<br>

### 1.1 조건문
- 참/거짓을 판단할 수 있는 **조건식**과 함께 사용함
    - ex) *26도 이상*이면 에어컨을 가동한다 -> *'26도 이상'* 이부분이 조건식
- 조건이 참인 경우 **if** 이후 들여쓰기 되어있는 코드 블록 실행
- if가 참이 아닌경우 **elif**를 이용하여 다음 조건을 제시할 수 있음
    - **elif**는 여러개 사용 가능
- 이외의 경우 **else** 이후 들여쓰기 되어있는 코드 블록 실행
    - else는 필요한 경우가 아닐 때 생략 가능
```python
if '첫번째 조건식':
    '첫번째 조건식이 참이면 실행'
elif '두번째 조건식':
    '첫번째 조건식이 참이 아닌경우 두번째 조건식을 확인하고 참일 경우 실행'
elif '세번째 조건식':
    '첫번째, 두번째 조건식이 모두 거짓이고, 세번째 조건식이 참인 경우 실행'
else:
    '위 모든 조건식이 거짓일 경우 실행'
```
> *하나의 조건문은 if로 시작해서 else로 끝나는데 그 도중에 여러개의 elif가 있을 수 있다. 다만, 하나의 조건문 안에서 조건식을 만족하는 조건문이 발생한다면 이후 조건식은 확인하지 않음을 유의!*

<br>

- 조건문은 다른 조건문에 중첩되어 사용 가능(**중첩 조건문**)
> *들여쓰기에 유의!*
```python
if '첫번째 조건식':
    '첫번째 조건식이 참이면 실행'
    if '두번째 조건식':
        '첫번째, 두번째 조건식 참이면 실행'
```

<br>

- **조건 표현식**
    - 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용
    - 삼항 연산자로 부르기도 함
    ```python
    '조건이 참일 때 값' if '조건' else '조건이 거짓일 때 값'
    ```
<br>

**퀴즈**
*아래 코드를 조건 표현식을 이용하여 나타내시오*
```python
num = 2
if num % 2 :
    result = '홀수'
else:
    result = '짝수'
print(result)

# 짝수
```

```python
num = 2
result = '홀수' if num % 2 else '짝수'
print(result)

# 짝수
```

<br>

### 1.2 반복문

- 특정 조건을 만족할 때까지 같은 동작을 반복
- **while 문**
    - 종료 조건에 해당하는 코드가 나올 때 까지 반복
- **for 문**
    - 반복 가능한 객체를 모두 순회하면 종료
- **반복 제어**
    - break, continue, for-else

<br>

#### 1.2.1  while 문
- 조건이 참일 때 들여쓰기 되어 있는 코드 블록 실행
- 코드 블록을 모두 실행한 뒤, 조건식으로 돌아감
- 무한 루프를 돌지 않게 **종료 조건이 반드시 필요**
- 복합연산자로 연산과 할당을 같이 진행
    ```python
    cnt = 0
    while cnt == 10:    # 횟수가 10되면 그만
        cnt += 1        # 횟수 + 1
        print(cnt)
    ```
<br>

#### 1.2.2 for 문
- for문은 시퀀스를 포함한 순회 가능한 객체의 요소를 모두 순회함
    - 처음부터 끝까지 모두 순회하기 때문에 별도의 종료 조건 필요 X
    - 순회 가능한 객체 : string, list, dict, tuple, range, set 등
    ```python
    for animal in ['dog', 'cat', 'bird']:
        print(animal)
    print('end')

    '''
    dog
    cat
    bird
    end
    '''
    ```

    - string은 하나의 문자 단위로 입력받음
    ```python
    word = 'python'
    for char in word:
        print(char)
    print('end')

    '''
    p
    y
    t
    h
    o
    n
    '''
    ```

    - dictionary는 기본적으로 key를 순회(key를 이용하여 값을 활용)
    ```python
    ages = {'junhyuk' : 30, 'chanju' : 26, 'misook' : 60}
    for name in ages:
        print(name, ages[name])
    
    '''
    junhyuk 30
    chanju 26
    misook 60
    '''
    ```

    - 혹은, items() 메소드를 활용
    ```python
    ages = {'junhyuk' : 30, 'chanju' : 26, 'misook' : 60}
    for name, age in ages:
        print(name, age)
    
    '''
    junhyuk 30
    chanju 26
    misook 60
    '''
    ```

    <br>

    - enumerate 순회
        - index와 객체를 쌍으로 담은 열거형 객체로 변환
        - 기본적으로 index는 0부터 시작하지만 start 옵션을 이용하여 변경 가능
        ```python
        members = ['junhyuk', 'chanju', 'misook']
        print(list(enumerate(members))) 
        
        # [(0, 'junhyuk'),(1, 'chanju'),(2, 'misook')]
        
        print(list(enumerate(members), start = 1)) 
        
        # [(1, 'junhyuk'),(2, 'chanju'),(3, 'misook')]
        ```
        > *enumerate를 사용 시 list와 같이 써줘야 객체 반환 가능*
    
    <br>

    - List Comprehension
        - 표현식과 제어문을 이용하여 특정한 값을 가진 리스트를 간결하게 생성하는 방법
        ```python
        # 1~3의 세제곱 리스트
        cubic_list = []
        for number in range(1, 4):
            cubic_list.append(number ** 3)
        print(cubic_list)

        # [1, 8, 27]
        ```
        ```python
        cubic_list = [number ** 3 for number in range(1, 4)]
        print(cubic_list)

        # [1, 8, 27]
        ```

    <br>

    - 반복문 제어
        - break : 반복문 종료
        - continue : continue 이후의 코드 블록은 수행하지 않고 다음 반복문 실행
        - for-else : 끝까지 반복문을 실행한 이후에 else 문 실행
            - break를 통해 중간 종료 시 else 문 실행되지 않음
            ```python
            for char in 'apple':
                if char == 'b':
                    print('b!')
                    break
            else:
                print('b is not in word')
            
            # b is not in apple

            for char in 'banana':
                if char == 'b':
                    print('b!')
                    break
            else:
                print('b is not in word')

            # b!
            ```

        
        - pass : 아무것도 하지 않음(문법적으로 필요할 때 사용)

<br>

## 2. 함수
- 함수는 Decomposition(분해)와 Abstraction(추상화)를 위해 사용
    - Decomposition : 기능을 분해하고 재사용 가능하게 만듬
    - Abstraction : 복잡한 내용을 몰라도 사용 가능하게 함

<br>

### 2.1 함수의 기초

#### 함수의 정의

- 함수는 특정한 기능을 하는 코드의 조각으로 특정 코드를 매번 다시 작성하지 않고, 필요할 때 호출하여 간편하게 사용함

<br>

#### 함수의 종류

- 함수는 **내장 함수**, **외장 함수**, **사용자 정의 함수** 3 가지로 분류됨
- **내장 함수** : 파이썬에 기본적으로 포함된 함수
- **외장 함수** : import를 통해 사용하며, 외부 라이브러리에서 제공하는 함수
- **사용자 정의 함수** : 사용자가 직접 만드는 함수

<br>

#### 함수의 기본 구조
- **선언과 호출(define & call)**
    - 함수의 선언은 **def** 키워드를 활용
    - 들여쓰기를 통해 function body를 작성
    - 함수를 설명하는 **Docstring**은 함수 body 앞에 선택적으로 작성 가능
    - ''''''을 이용
    - 함수는 parameter를 넘겨줄 수 있음
    - 함수는 동작 후 return을 통해 결괏값을 전달
    ```python
    def func_a(parameter):
        # code block
        return returning_value
    ```
    - 함수는 함수명()으로 호출하여 사용
        - parameter가 있는 경우에 함수명(parameter1, parameter2...)로 호출
    ```python
    num1 = 0
    num2 = 1
    def func_add(a, b):
        return a + b
    
    def func_sub(a, b):
        return a - b
    
    def func_a(a, b):
        return func_add(a, 5) + func_sub(5, b)

    result = func_a(num1, num2)
    print(result) # 9
    ```

- **입력(input)**
    - **Parameter** : 함수를 정의할 때, **함수 내부**에서 사용되는 변수
    - **Argumernt** : 함수를 호출 할 때, 넣어주는 값
    ```python
    def function(para): # parameter : para
        return para
    
    function('argu') # argument : 'argu'
    # 함수 리턴 값 : argu
    ```
    - **positional arguments**
        - 기본적으로 함수 호출 시 argument는 위치에 따라 전달
        ```python
        def add(x, y):
            return x + y
        
        add(2, 3)   # 5(x = 2, y = 3으로 할당)
        ```

    - **keyword arguments**
        - 직접 변수의 이름으로 특정 algument를 전달할 수 있음
        - keyword argument 다음에 positional argument 사용 불가
        ```python
        def add(x, y):
            return x + y
        
        add(x=2, y=3)   # 5
        add(2, y=3) # 5
        add(x=2, 5) # Error
        ```
    - **Default Arguments Values**
        - 기본값을 지정하여 함수 호출 시 argument 값을 설정 하지 않아도 됨
        - 정의된 것 보다 적은 개수의 argument 들로 함수 호출 가능
        ```python
        def add(x, y=3):
            return x + y

        add(2)  # 5(x = 2를 받고, y = default값인 3을 받음)
        ```
        > 단, default로 지정되어 있는 값도 argument를 다시 주는것 가능함!
    
    <br>

    - **가변 인자(\*args)**
        - 여러 개의 positional argument를 하나의 필수 parameter로 받아서 사용
        - 몇 개의 positional argument를 받을지 모르는 함수를 정의할 때 유용
        ```python
        def add(*args):
            result = 0
            for arg in args:
                result += arg
            return result

        add(2)  # 2
        add(2, 3, 4, 5) # 14
        ```
        <br>

        - **가변 인자 예시**
            -  반드시 받아야하는 인자, 추가적인 인자를 구분해서 사용 가능
            ```python
            def print_family_name(father, mother, *pets):
                print(f'아버지 : {father}')
                print(f'어머니 : {mother}')
                print('반려동물들 ..')
                for pet in pets:
                    print(f'반려동물: {pet}')
            ```

    - **패킹 / 언패킹**
        
        - 패킹 : 여러 개의 데이터를 묶어서 변수에 할당하는 것
        ```python
        numbers = (1, 2, 3, 4, 5)   # 패킹
        print(numbers)  # (1, 2, 3, 4, 5)
        ```
        - 언패킹 : 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
        ```python
        numbers = (1, 2, 3, 4, 5)
        a, b, c, d, e = numbers # 언패킹
        print(a, b, c, d, e)    # 1 2 3 4 5
        ```
        - 응용
        ```python
        numbers = (1, 2, 3, 4, 5)   # 패킹

        a, b, *rest = numbers   # 1, 2를 제외한 나머지 rest에 대입
        print(a, b, rest)   # 1 2 [3, 4, 5]
        ```
    
    <br>

    - **가변 키워드 인자(kwargs)**
        - 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
        - \*\*kwargs는 딕셔너리로 묶여 처리되며, parameter에 \*\*를 붙여 표현
        ```python
        def family(**kwargs):
            for key, value in kwargs.items():
                print(key, ":", value)
        
        family(father= '아빠', mother= '엄마', pet= '강아지')
        '''
        father : 아빠
        mother : 엄마
        pet : 강아지
        '''
        ```

    <br>

- **결괏값(Output)**
    - 결괏값에 따라서 Void function, Value returning function으로 나뉨
    - Void function : 명시적인 return값이 없는 경우, None을 반환하고 종료
    - Value returning function : 함수 실행 후, return문을 통해 값 반환
        - return을 하게 되면, 값 반환 후 함수 바로 종료
    > *print와 return의 차이점!*
    > print를 사용하면 호출될 때마다 값이 출력(주로 테스트를 위해 사용)
    > 데이터 처리를 위해서는 return을 사용해야함
    - 두 개 이상의 값도 반환이 가능
        - 반환 값으로 튜플을 사용(return값 변경을 방지하기 위해)
        ```python
        def minus_and_product(x, y):
            return x - y, x * y
        
        y = minus_and_product(4, 5)
        print(y)    # (-1, 20)
        print(type(y))  # <class 'tuple'>
        ```

- **범위(Scope)**
    - 함수는 코드 내부에 **local scope**를 생성하고, 그 외 공간은 **global scope**

        - **loacl scope** : 함수가 만든 scope로 함수 내부에서만 참조 가능
        - **global scope** :  코드 어디에서든 참조할 수 있는 공간
    - 마찬가지로 variable도 local과 global이 있음
        - **local variable** : local scope에 정의된 변수
        - **global variable** : global scope에 정의된 변수
    ```python
    def func():
        a = 10
        print('local', a)   # local 10
    func()
    print('global', a)  # NameError: name 'a' is not defined
    ```

    
    - **변수 수명주기**
        - build-in scope : 파이썬이 실행된 이후부터 영원히 유지
        - global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
        - local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
    
    - **이름 검색 규칙**
        - 파이썬에서 사용되는 이름은 namespace에 저장되어 있음
        - LEGB Rule이라고 불리는 순서가 존재
            - Local scope : 지역범위(현재 작업 중인 범위)
            - Enclosed scope : 지역 범위의 한 단계 위 범위
            - Global scope : 최상단에 위치한 범위
            - Built-in scope : 모든 것을 담고 있는 범위
        - **함수 내부에서는 바깥 Scope의 변수에 접근은 가능하지만 수정은 불가**
        - LEGB 예시
        ```python
        a = 0
        b = 1
        def enclosed():
            a = 10
            c = 3
            def local(c):
                print(a, b, c)  # 10 1 300
            local(300)
            print(a, b, c)  # 10 1 3
        enclosed()
        print(a, b) # 0 1 
        ```
        <br>

    - **global 문**
        - 현재 코드 블록 전체에 적용되며, 나열된 식별자가 global variable임을 나타냄
            - global에 나열된 식별자는 같은 코드 블록에서 global 앞에 등장할 수 없음
            - global에 나열된 식별자는 parameter, for 루프, 클래스/함수에 정의될 수 없음
        ```python
        a = 10
        def func_1():
            global a
            a = 3
        
        print(a)    # 10
        func_1()
        print(a)    # 3
        ```
        - global 관련 에러
        ```python
        a = 10
        def func_1():
            print(a)    # global a 선언 전에 사용
            global a
            a = 3
        
        print(3)
        func_1()
        print(a)    # SyntaxError
        ```
        ```python
        a = 10
        def func_1(a):
            global a    # parameter에 global 사용 불가
            a = 3
        
        print(a)
        func_1(1)
        print(a)    # SyntaxError
        ```
    
    - **nonlocal**
        - global을 제외하고 가장 가까운 scope의 변수를 연결하도록 함
            - global과 같은 특징 가짐(parameter X 등등)
        - global과는 달리 이미 존재하는 이름과의 연결만 가능

        ```python
        x = 0
        def func_1():
            x = 1
            def func_2():
                nonlocal x
                x = 2
            func_2()
            print(x)    # 2
        
        func_1()
        print(x)    # 0
        ```

        <br>

    - **함수의 범위 주의!!!**
        - 기본적으로 함수에서 선언된 변수는 local scope에 생성, 함수 종료 시 사라짐
        - 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색
            - 단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨받아 활용
        - 상위 scope에 있는 변수를 수정하고 싶다면 global, nonloacl 활용

    <br>

#### 함수의 응용
- **map**
    - **map(function, iterable)**
    - 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
    ```python
    n, m = map(int, input().split())    #1, 2를 입력하면
    print(n, m) # 3, 5
    print(type(n), type(m)) # <class 'int'> <class 'int'>
    ```

- **filter**
    - **filter(function, iterable)**
    - 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 
    그 결과가 True인 것들을 filter object로 반환
    ```python
    def odd(n):
        return n % 2
    numbers = [1, 2, 3]
    result = filter(odd, numbers)
    print(result, type(result)) # <filter object ad ~~~~> <class 'filter'>
    print(list(result)) # [1, 3]
    ```

- **zip**
    - **zip(\*iterables)**
    - 복수의 iterable을 모아 튜플을 원소로 하는 zip object 반환
    ```python
    cats = ['mir', 'choco']
    dogs = ['chancho', 'hodu']
    pair = zip(cats, dogs)
    print(pair, type(pair)) # <zip object at ~~~~> <class 'zip'>
    print(list(pair))   # [('mir, 'chancho'), ('choco', 'hodu')]
    ```

- **lambda**
    - **lambda[parameter] : 표현식**
    - 표현식을 계산한 결과를 반환하는 함수로, 익명함수라고도 불림
    - return문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
    - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
    - def를 사용할 수 없는 곳에서도 사용 가능
    ```python
    # 삼각형의 넓이를 구하는 공식
    def triangle_area(b, h):
        return 0.5 * b * h
    print(triangle_area(5, 6))  # 15.0

    # lambda 이용
    triangle_area = lambda b, h : 0.5 * b * h
    print(triangle_area(5, 6))  # 15.0
    ```

- **재귀 함수(recursuve function)**
    - 자기 자신을 호출하는 함수
    - 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
    - 점화식에 많이 사용
    - 변수의 사용이 줄어들어 코드의 가독성 증가
    - 1개 이상의 base case(종료되는 상황)이 존재하고, 수렴하도록 작성 필요
    - 메모리 스택이 넘치게 되면 프로그램이 동작하지 않게 됨
    (파이썬에서는 최대 재귀 깊이가 1000번으로 호출 횟수가 이를 넘어가면 에러 발생)
    ```python
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    print(factorial(4)) # 24
    ```
    <br>

    재귀 함수 -> 반복문
    ```python
    def fact(n):
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
    
    print(fact(4))  # 24
    ```

    - 재귀 함수 <-> 반복문(서로 대체 가능)
        - 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수 사용
        - 재귀 호출은 변수 사용 줄이기 가능
        - 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림

