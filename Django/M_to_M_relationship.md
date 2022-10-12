## M:N
- many-to-many relationships
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우

target model
- 관계 필드를 가지지 않은 모델

source model
- 관계 필드를 가진 모델 


## 중개 모델
- 환자와 의사의 예약 관리 테이블에서 정보를 가져와 예약 테이블을 따로 만들어서 운영하는 방식


## ManyToManyField
- 중개 테이블을 자동으로 생성
- 두 모델 어디에 위치해도 상관없지만, 참조와 역참조는 주의!
- 다대다 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자가 필요(M:N 관계로 설정할 모델 클래스)
- 모델 필드의 RelatedManager를 사용하여 개채 추가, 제거 가능
    - add(), remove(), create(), clear()...
- 'db_table' arguments를 사용하여 중개 테이블 이름 변경 가능


```python
# models.py

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()

```

- related_name
    - target model이 source model을 참조할 때 사용할 manager name
    - ForignKey의 related_name과 동일
- through
    - 중개 테이블을 직접 작성하는 경우, through 옵션으로 중개 테이블을 나타내는 장고 모델 지정
- symmetrical
    - default: True
        - _set 매니저 추가 X
        - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동 참조
        - 대칭을 원하지 않는 경우 False로 설정
    - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
    - 팔로우 기능, 좋아요 기능

## Related Manager
- 장고는 모델 간 N:1, N:M 관계가 설정되면 역참조시에 사용할 수 있는 manager를 생성
- 같은 이름의 메서드여도 각 관계에 따라 다르게 사용됨
    - N:1에서는 target 모델 객체만 사용 가능
    - N:M은 두 모델 다 사용 가능
- add(), remove(), create(), clear(), set()...

## LIKE 기능 구현
- ManyToManyField 작성
```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10)
    .
    .
    .
```
이대로 진행하면 에러 발생
- like_users 필드 생성 시 자동으로 역참조에는 article_set 매니저가 생성
- 하지만 이미 article - user 관계에서 사용하고 있는 매니저
- 두 매니저 구분이 안되기 때문에 N:M 구조의 매니저 이름을 변경해야 함(related_name)
```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    .
    .
    .
```