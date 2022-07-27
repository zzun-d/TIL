# 5. OOP(객체지향 프로그래밍)
---

## 5.1 객체 지향 프로그래밍
- **OOP(Object Oriented Programming)**
- 프로그래밍의 패러다임
- 컴퓨터 프로그램을 명령어의 목록으로 보지 않고, 여러 개의 독립된 단위로 봄
    - 예시)
        - EPL
            - 토트넘 객체
            - 리버풀 객체
            - 맨시티 객체
<br>

- 즉, 하나의 프로그램 내에 여러 **'객체'** 들의 모임으로 파악
    - 객체
        - 변수(정보)
        - 함수(행동)

<br>

- 각각의 객체는 메시지를 주고받고, 데이터 처리가 가능
- 객체지향 프로그래밍 <-> 절차지향 프로그래밍
    - 절차지향 프로그램은 한 부분을 변경하면 다 연쇄작용으로 수정이 필요
    - 객체지향 프로그래밍은 **부분만 수정이 가능(데이터와 기능의 분리 / 추상화된 구조)**
        - 추상화?
            - 복잡한 것은 숨기고, 필요한 것은 들어냄

<br>

- **객체지향의 장/단점**
    - 장점
        - 클래스 단위로 모듈화 -> 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
        - 필요한 부분만 수정하기 쉬워서 프로그램 유지보수 용이
    - 단점
        - 설계할 때 많은 노력과 시간이 필요
        > 객체들의 상호 작용 구조를 생각하고 코드 작성하는 것이 어려움
        - 실행 속도가 상대적으로 느림
        > 절차 지향 프로그래밍이 컴퓨터 처리구조와 비슷하여 실행 속도가 더 빠름

<br>

## 5.2 객체(Object)
- 클래스에서 정의한 것을 토대로 메모리에 할당된 것
- 쉽게 말하면, **속성과 행동으로 구성된 모든 것**을 뜻함
- 예시)
    - 객체 - 손흥민

    |속성(변수)|행동(함수-메서드)|
    |:---:|:---:|
    |직업<br>축구 선수|패스하기()<br>전방 쓰루패스!|
    |나이<br>1992년 생|슛하기()<br>왼발 감아차기!|
    |소속<br>토트넘 홋스퍼|세레모니()<br>찰칵! 손가락 세레모니|

    - 축구 선수 -> 클래스

<br>

- **객체와 인스턴스**
    - 클래스로 만든 객체를 인스턴스라 함

        - 손흥민은 객체다(O)
        - 손흥민은 인스턴스다(X)
        - 손흥민은 축구선수의 인스턴스다(O)

<br>

- **파이썬은 모든 것이 객체로 이루어짐**
    - **속성과 행동이 존재!!**
    - 리스트, 문자열 모두 객체이며 .sort(), .upper()등의 메소드가 행동
    - 객체가 무엇인지(str, int, list, iterable) -> 정보
    - 객체를 안고 있는 큰 범주 -> class
        - ex)
            - 123, 1000, 0 -> int(class)의 인스턴스
            - 'good', 'boy' -> str(class)의 인스턴스

<br>

### 정리!!
> - 객체(object)의 특징
>   - 타입(type): 어떤 operator와 method가 가능한가?
>   - 속성(attribute): 어떤 data를 가지는가?
>   - 조작방법(method): 어떤 행동(함수)을 할 수 있는가? <br>
>    **객체(Object) = 속성(Attribute) + 기능(Method)**
> <br>

<br>

## 5.3 객체와 클래스 문법

- **기본 문법**
    - 클래스 정의: `class MyClass:`
    - 인스턴스 생성: `my_instance = MyClass()`
    - 메서드 호출: `my_instance.my_method()`
    - 속성: `my_instance.my_attribute`

<br>

- **클래스, 인스턴스**
    - 객체의 클래스를 가지고, 객체 생성
    - 클래스: 객체들의 분류 / 설계도
    - 인스턴스: 하나하나의 실체 / 인스턴스(예)
    ```python
    class Person:
        pass
    print(type(Person)) # <class 'type'>
    person_1 = Person()
    print(isinstance(person_1, Person)) # True
    print(type(person_1))   # <class '__main__.Person'>
    ```

<br>

- **객체 비교하기**
    - ==
        - **동등**한 객체인지
        - 변수가 참조하는 객체가 내용이 같은 경우 True
        - 두 객체가 같아 보이지만 **실제로 동일한 대상을 가리킨다고 확인한 것은 아님**
    - is
        - **동일**한 객체
        - 두 변수가 동일한 객체를 가리키는 경우 True
    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b, a is b) # True, False
    # 동일해 보이지만, 실제 메모리 저장은 따로 되어있음

    a = [1, 2, 3]
    b = a
    print(a == b, a is b)   # True, True
    # a가 가리키는 주소를 b도 가리키기 때문에 완전 동일한 객체
    ```


<br>

- **속성(데이터, 정보, 상태)**
    - 특정 데이터 타입/클래스의 객체가 가지게 될 상태나 데이터를 의미함
    - 클래스 변수와 인스턴스 변수가 존재
    ```python
    class Person:
        blood = '빨강'  # 클래스 변수

        def __init__(self, name):
            self.name = name    # 인스턴스 변수

    person_1 = Person('흥민')
    print(person_1.name)    # 흥민
    ```

    <br>

    - 인스턴스 변수
        - 인스턴스가 가진 개인적인 속성 및 고유 변수
        - 생성자 메서드(__init__)에서 self.<name>으로 정의함
        - 
        ```python
        class Person:

        def __init__(self, name, gender):   # 인스턴스 변수 정의
            self.name = name    
            self.gender = gender

        heungmin = Person('seungmin', 'male')
        print(heungmin.name)    # heungmin
        heungmin.name = 'Heungmin Son'
        print(heungmin.name)    # Heungmin Son
        ```

    <br>

    - 클래스 변수
        - 클래스 선언 내부에서 정의 함
        - <classname>.<name>으로 접근 및 할당 가능
        ```python
        class Person():
            blood = '빨강'  # 클래스 변수 정의

            def __init__(self, name):
                self.name = name    # 인스턴스 변수
        
        person_1 = Person('Sony')
        person_2 = Person('Kein')

        print(Person.blood)     # 빨강
        print(person_1.blood)   # 빨강
        print(person_2.blood)   # 빨강

        # 클래스 변수를 변경
        Person.blood = '파랑' 
        print(Person.blood)     # 파랑
        print(person_1.blood)   # 파랑
        print(person_2.blood)   # 파랑

        # 인스턴스 변수를 변경
        person_1.blood = '초록'
        print(Person.blood)     # 파랑
        print(person_1.blood)   # 초록
        print(person_2.blood)   # 파랑

        # 클래스 변수를 변경할 때는 항상 클래스.클래스변수 형식으로 변경
        ```
  
    <br>

    - 클래스 변수 활용
        - 사용자가 몇명인지 확인하고 싶을 때
            - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정이 가능
            ```python
            class Person():
                count = 0

                def __init__(self, name):
                    self.name = name 
                    Person.count += 1   # __init__함수가 호출 될 때마다 count에 1씩 더함
            
            person_1 = Person('Sony')
            person_2 = Person('Kein')

            print(Person.count) # 2
            ```
    <br>

## 5.4 메서드
- 특정 데이터 타입이나 클래스의 객체에 공통적으로 적용 가능한 행위(함수)
- 클래스 안에 있는 함수
<br>

- **인스턴스 메서드**
    - 인스턴스의 영역에서 인스턴스를 처리하는 메서드
    - 인스턴스의 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
    - 클래스 내부에 정의되는 메서드의 기본
    - 호출 시에 첫번째 인자로 자기자신(self)이 전달
    ```python
    class Person:
        def instance_method(self, name):
            pass

    person_1 = Person()
    person_1.instance_method(name)
    # person_1은 instance_method의 self로 들어감!
    ```
    - **self**
        - 인스턴스 자기자신
        - 매개변수 이름으로 self를 첫 번째 인자로 정의한 것
    
    <br>

    - **생성자 메서드**
        - \_\_init\_\_
        - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
        - 인스턴스 변수의 초기값 설정
            - 인스턴스 생성, __init__메서드 자동 호출
        - 매직 메서드 중 하나
            > - Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
            > - 스페셜 메서드라고도 불림
            > - 특정 상황에 자동으로 불리는 메서드
            > - \_\_str\_\_: 해당 객체의 출력 형태를 지정
            >    - 프린트 함수를 호출할 때, 자동으로 호출
            >    - 어떤 인스턴스를 출력하면 \_\_str\_\_의 return 값이 출력
            > - \_\_gt\_\_: 부등호 연산자(>, greater than)
            > 등이 있으며, Django에서 사용할 예정!
            ```python
            class Person:
                def __init__(self, name, pay):
                    self.name = name
                    self.pay = pay
                
                def salary(self):
                    return self.pay * 12
                
                def __str__(self):
                    return f'[선수] 월급: {self.pay}'
                
                def __gt__(self, other):
                    return self.pay > other.pay
            
            person_1 = Person('Sony', 20000)
            person_2 = Person('Kein', 10000)

            print(person_1) # [선수] 월급: 20000
            print(person_2) # [선수] 월급: 10000
            print(person_1 > person_2)  # True
            print(person_1 < person_2)  # False
            ```

    <br>

    - **소멸자 매서드**
        - 인스턴스 객체가 소멸되기 직전에 호출되는 메서드
        ```python
        class Peraon:
            def __del__(self):
                print('인스턴스 삭제!')

        person_1 = Person()
        del person_1    # 인스턴스 삭제!
        ```
    
    

<br>

- **클래스 메서드**
    - 클래스의 영역에서 클래스를 처리하는 메서드
    - @classmethod 데코레이터를 사용하여 정의
        - 데코레이터
            - 함수를 어떤 함수로 꾸며서 새로운 기능 부여
            - @함수명 형태로 함수 위에 작성
            - 순서대로 적용! 순서가 중요함!
        ```python
        # 데코레이터 없이 함수 꾸미기
        def hi():
            print('hi')
            
        def add_print(original):    # 파라미터로 함수를 받고
            def wrapper():          # 함수 내에서 새로운 함수 선언 
                
                # 오리지날을 위 아래로 꾸미는 부가적 기능
                print('method start')
                original()
                print('method end')
            return wrapper
        
        add_print(hi)()
        # method start
        # hi
        # method end

        # 데코레이터로 함수 꾸미기
        @add_print
        def print_hi():
            print('hi')
        
        print_hi()
        # method start
        # hi
        # method end
        ```
    
    <br>

    - 호출 시에 첫번째 인자로 클래스(cls)가 전달 됨
    ```python
    class Person:
        count = 0

        def __init__(self, name):
            self.name = name
            Person.count += 1
        
        @classmethod
        def person_num(cls):
            print(f'사람은 모두 {cls.count}명입니다.')
    
    person_1 = Person('Sony')
    person_2 = Person('kein')
    print(Person.count) # 2
    Person.person_num() # 사람은 모두 2명입니다.
    ```

<br>

**정리!**
> - 클래스 메서드는 클래스 변수 사용
> - 인스턴스 메서드는 인스턴스 변수 사용
> - 둘 다 쓰고 싶을 땐, 인스턴스 메서드 사용
>   (클래스 메서드는 인스턴스 변수 사용이 불가능하기 때문)


<br>

- **정적 메서드** 
    - 클래스, 인스턴트와 상관없는 메서드
        - 객체 상태나 클래스 상태를 수정할 수 없는 메서드
    - @staticmethod 데코레이터를 사용하여 정의
    - 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속
        - 주로 해당 클래스로 한정하는 용도로 사용 됨

- **인스턴스와 클래스 간의 이름 공간(namespace)**
    - 클래스를 정의하면, 해당하는 이름 공간 생성
    - 인스턴스도 마찬가지로 해당하는 이름 공간 생성
    - 인스턴스에서 특정한 속성에 접근하면, 인스턴스탐색 후 클래스 탐색
    ```python
    class Person:
        name = 'Sony'

        def tall(self):
            print(self.name)

    # 인스턴스 변수가 없기 때문에 class 변수가 출력 됨
    person_1 = Person()
    person_1.tall() # Sony

    # 인스턴스 변수를 정의하여 인스턴스 변수가 출력 됨
    person_2 = Person()
    person_2.tall() # Sony
    person_2.name = 'Kein'
    person_2.tall() # Kein

    # Person 클래스의 값이 Kein으로 변경된 것이 아니라 
    # person_2 인스턴스 이름 공간에 name이 Kein으로 저장된 것
    print(Person.name)  # Sony
    print(person_1.name)    # Sony
    print(person_2.name)    # Kein
    ```

<br>

**메서드 정리**

```python
class MyClass:
    def method(self):
        return 'instance metod', self

    @classmethod
    def classmethod(cls):
        return 'class method', cls

    @staticmethod
    def staticmethod()"
    return 'staticmethod'

# 인스턴스 메서드 호출 결과
obj_1 = MyClass()
print(obj_1.method()) # ('instance metod', <__main__.MyClass object at 0x000001AC0AFEA3E0>)
print(MyClass.method(obj_1))  # ('instance metod', <__main__.MyClass object at 0x000001AC0AFEA3E0>)

# 클래스 자체에서 각 메서드 호출
print(MyClass.classmethod())    # ('class method', <class '__main__.MyClass'>)
print(MyClass.staticmethod())   # staticmethod
MyClass.method()    # TypeError: MyClass.method() missing 1 required positional argument: 'self'

# 인스턴스는 클래스 메서드, 스태틱 메서드 모두 접근 가능
print(obj_1.classmethod())      # ('class method', <class '__main__.MyClass'>)
print(MyClass.classmethod())    # ('class method', <class '__main__.MyClass'>)
print(obj_1.staticmethod())     # staticmethod

```

<br>

## 5.5 객체 지향의 핵심개념
**추상화, 상속, 다형성, 캡슐화 4 가지가 핵심개념**
<br>

### 1. **추상화**
<br>

- 현실 세계를 프로그램 설계에 반영한 것으로
- 복잡한 것 숨기고 필요한 것만 생성

<br>

### 2. **상속**

<br>

- 두 클래스 사이 부모-자식 관계 정립
- 클래스는 상속이 가능하다
- 모든 파이썬의 클래스들은 object를 상속 받는다.
- class ChildClass(ParentClass)로 상속 받을 수 있음
- 자식 클래스는 부모 클래스에 정의된 속성, 행동, 관계, 제약 조건을 모두 상속 받음
- 코드의 재사용성 증가
- 상속의 사용 이유를 예로 살펴보자
    ```python
    class Person:

        def __init__(self, name, age):
            self.name = name    # 인스턴트 변수
            self.age = age
        
        def talk(self): # 인스턴트 메서드
            print(f'안녕하세요. 제 이름은 {self.name}입니다.')  
        
    student = Person('이학생', 28)
    student.talk()  # 안녕하세요. 제 이름은 이학생입니다.

    professor = Person('김교수', 50)
    professor.talk()    # 안녕하세요. 제 이름은 김교수입니다.

    # 교수와 학생을 구분하고 싶음

    class Professor:
        def __init__(self, name, age, job):
            self.name = name
            self.age = age
            self.job = job

        def talk(self): # 중복됨
            print(f'안녕하세요. 제 이름은 {self.name}입니다.')

    class Student:
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department

        def talk(self): # 중복됨
            print(f'안녕하세요. 제 이름은 {self.name}입니다.')

    professor = Professor('김교수', 50, '교수')
    professor.talk()    # 안녕하세요. 제 이름은 김교수입니다.

    sturdent = Student('이학생', 28, '소프트웨어')
    student.talk()  # 안녕하세요. 제 이름은 이학생입니다.

    # 공통 부분을 계속 쓰기 불편    
    # 상속을 사용!

    class Person:

        def __init__(self, name, age):
            self.name = name    # 인스턴트 변수
            self.age = age
        
        def talk(self): # 인스턴트 메서드
            print(f'안녕하세요. 제 이름은 {self.name}입니다.')  

    class Professor(Person):
        def __init__(self, name, age, job):
            self.name = name
            self.age = age
            self.job = job

    class Student(Person):
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department

    professor = Professor('김교수', 50, '교수')
    professor.talk()    # 안녕하세요. 제 이름은 김교수입니다.

    sturdent = Student('이학생', 28, '소프트웨어')
    student.talk()  # 안녕하세요. 제 이름은 이학생입니다.
    ```
<br>

- 상속 관련 함수와 메서드
    - isinstance(object, classinfo)
        - classinfo의 instance거나 subclass인 경우에 True
        위 코드의 경우
        ```python
        # 상속 전 
        isinstance(student, Person) # False

        # 상속 후
        isinstance(student, Person) # True
        ```
    - issubclass(class, classinfo)
        - class가 classinfo의 subclass면 True
        ```python
        issubclass(bool, int)   # True
        issubclass(Student, Person) # True
        issubclass(Student, Professor)  # False
        issubclass(Student, (Professor, Person))  # True
        # classinfo는 튜플 형태일 수 있으며, 하나 하나 확인하여 sub가 있으면 True
        ```
    - super()
        - 자식클래스에서 부모클래스를 사용하고 싶을 때
        ```python
        class Person:
            def __init__(self, name, age, gender, phone_number):
                self.name = name
                self.age = age
                self.gender = gender
                self.phone_number = phone_number

        class Professor(Person):
            def __init__(self, name, age, gender, phone_number, job):
                self.name = name
                self.age = age
                self.gender = gender
                self.phone_number = phone_number
                self.job = job

        # 상속받는 매개변수를 일일이 써주기 귀찮음...
        # super를 이용

        class Person:
            def __init__(self, name, age, gender, phone_number):
                self.name = name
                self.age = age
                self.gender = gender
                self.phone_number = phone_number

        class Professor(Person):
            def __init__(self, name, age, gender, phone_number, job):
                # Person Class의 __init__ 사용
                super().__init__(name, age, gender, phone_number)
                self.job = job

        ```
    - mro(), Method Resolution Order
        - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
        - 기존 인스턴스, 자식 클래스, 부모 클래스로 확장
        - classname.mro()로 사용

<br>

**상속정리**
> 파이썬의 모든 클래스는 object가 부모 클래스(object로부터 상속)
> 부모 클래스의 모든 속성과 메서드를 상속 받음
> super() 함수를 이용해 부모 클래스의 요소를 받아올 수 있음
> 메서드 오버라이딩을 이용하여 자식 클래스에서 메서드 재정의 가능
> 상속관계의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색함
<br>

- **다중 상속**
    - 두 개 이상의 클래스를 상속 받음
    - 상속 받은 모든 클래스의 요소 사용 가능
    - 중복된 속성이나 메서드 있을 경우에 상속 순서에 따라 결정(앞에 쓴게 우선)

<br>

### 3. **다형성**

- 여러 모양을 뜻함
- 동일한 메서드가 클래스에 따라서 다른 행동을 할 수 있음을 의미함
    - 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대하여 다른 방식으로 응답 가능
<br>

- **메서드 오버라이딩**
    - 상속받은 메서드를 재정의
    - 클래스 상속 시에 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경 하는 것
    - 부모 클래스의 메서드 이름과 기능은 그대로 사용하지만, 특정한 기능만 바꾸고 싶거나,
    기능을 추가하고 싶을 때 사용
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
        
        def talk(self):
            print(f'안녕하십니까. {self.name}입니다.')

    class Professor(Person):
        def talk(self):
            print(f'네 반가워요, {self.name}입니다.')
    
    class Student(Person):
        def talk(self):
            super().talk()
            print(f'교수님 잘 부탁드립니다.')
    
    stu = Student('이학생')
    stu.talk()
    # 안녕하십니까. 이학생입니다.
    # 교수님 잘 부탁드립니다.

    pro = Professor('김교수')
    pro.talk()
    # 네 반가워요, 김교수입니다.
    ```

### 4. 캡슐화
<br>

- 객체의 일부 구현 내용을 외부에서 접근하지 못하게 차단함(접근 제어)
    - 개인정보(주민등록번호, 계좌번호) 등등
<br>

- 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음
<br>

- 접근제어자의 종류
    - Public Access Modifier
        - 언더바 없이 시작하는 메서드나 속성
        - 어디서나 호출 가능, 하위 클래스에서 오버라이드 허용
        - 일반적으로 작성되는 메서드와 속성은 대부분 퍼블릭
        <br>

    - Protected Access Modifier
        - 언더바 1개로 시작하는 메서드나 속성
        - 암묵적 규칙에 의하여 부모 클래스 내부와 자식 클래스에서만 호출 가능
        - 하위 클래스 오버라이드 허용
        <br>

    - Private Access Modifier
        - 언더바 2개로 시작하는 메서드나 속성
        - 본 클래스 내부에서만 사용 가능
        - 하위클래스 상속, 호출 불가능(오류 발생)
        - 외부 호출 불가능(오류)
        <br>

    - getter와 setter 메서드
        - 변수에 접근할 수 있는 메서드를 별도로 생성
        - getter: 변수의 값을 읽는 메서드
            - @property 데코레이터를 사용
        - setter: 변수의 값을 설정하는 메서드
            - @변수.setter 사용
        
        ```python
        class Person:
            def __init__(self, age):
                self._age = age
            
            @property   # getter
            def age(self):
                return self._age
            
            @age.setter
            def age(self, new_age):
                if new_age > 31:
                    raise ValueError('Too Old For Study')
                    return

                self._age = new_age
        
        p = Person(20)
        print(p.age)    # 20

        p.age = 10
        print(p.age)    # 10

        p.age = 33
        print(p.age)    # ValueError: Too Old For Study
        ```

<br>

