# 1. Python Introduction
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
    - 함수는 동작 후 return을 통해 결과값을 전달
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
- **결과값(Output)**
- **범위(Scope)**