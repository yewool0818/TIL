# OOP (Object Oriented Programming)



[TOC]



## 1. 객체(Object)



#### 🤷‍♂️ 객체가 당최 뭐야?!

> Python에서 **모든 것**은 다 **객체**이다.

<br>

응? 🤢

객체에는 아래와 같은 것들이 속해있다!

> 1. 타입 ( `type` )
> 2. 속성 ( `attribute` )
> 3. 조작법 ( `method` )



**즉, 나만의 타입(Class)를 만들고,<br>**

**정보를 <u>속성으로(attribute)</u>,<br>**

**로직(행동)은 <u>메서드(method)로</u> 만드는 것이<br>**

**객체 지향 프로그래밍이다!**



<br>

🤸‍♂️ **객체의 특징**

- **타입(type)**: 어떤 연산자(`operator`)와 조작(`method`)이 가능한가?
- **속성(attribute)**: 어떤 `상태(데이터)`를 가지는가?
- **조작법(method)**: 어떤 `행위(함수)`를 할 수 있는가?



### 1.1. 타입



#### 1.1.1. 타입 (Type)

> 공통된 **`속성(attribute)`**과 **`조작법(method)`**를 가진 객체들의 분류



#### 1.1.2. 인스턴스 (Instance)

> - 특정 타입의 **실제 데이터 예시**이다.
>
> - 파이썬에서 모든 것은 객체이고, **모든 객체는 특정 타입의 인스턴스**이다.

<br>

>```python
>a = 10
>b = 20
>```
>
>- 위 코드에서 `a`와 `b`는 객체이다.
>- `a`와 `b`는 `int`타입의 인스턴스이다.

<br>

진짜인지 확인해보자! **타입 비교**

```python
type(a) == int  # True
type(b) == str  # False
```

<br>

### 1.2. 속성 (attribute) vs 메서드(method)

> **속성**
>
> : 객체(object)의 상태, 데이터
>
> <br>
>
> **메서드**
>
> : 특정 객체(object)에 적용할 수 있는 행위(조작법)

<br>

| 속성                        | 메서드                                          |
| :-------------------------- | ----------------------------------------------- |
| 객체(object)의 상태, 데이터 | 특정 객체(object)에 적용할 수 있는 행위(조작법) |
| `객체`.`속성`               | `객체`.`조작법`()                               |
| 3+4j.real                   | [3, 2, 1].sort()                                |



#### 1.2.1. 속성 활용 예제

> `complex` 타입 (복소수 타입) 인스턴스가 가진 속성을 확인해보자!

```python
# 복소수 생성 및 타입 확인
complex_number = 3+4j
print(type(complex_number)) # <class 'complex'>
```



> `complex` 타입 인스턴스가 가진 속성과 메서드들을 조회해보자

```python
print(dir(complex_number))
```

```
[..생략.. , '__truediv__', 'conjugate', 'imag', 'real']
```



> `imag` 속성과 `real` 속성을 활용해보자

```python
print("허수부: ",complex_number.imag)  # 허수부:  4.0
print("실수부: ",complex_number.real)  # 실수부:  3.0
```





#### 1.2.2. 메서드 활용 예제

> `list` 타입의 인스턴스에 적용 가능한 조작법(method)를 확인해보자.

```python
# 리스트 생성 및 타입 확인
a = [1, 2, 3]
print(type(a))  # <class 'list'>
```



> `complex` 타입 인스턴스가 가진 속성들과 메서드들을 조회해보자

```python
print(dir(a))
```

```
[..생략.., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```



> `sort` 메서드를 활용해서, 리스트를 정렬해보자
>
> 추가로 `pop`메서드를 이어서 활용할 수 있음을 확인해보자

```python
sorted_a = sorted(a)
print(sorted_a)       # [1, 2, 3]

pop_number = sorted(a).pop()
print(pop_number)     # 3
```





---

## 2. 클래스(Class)와 객체(Instance)

> **실생활 예시**
>
> 카페에서 바닐라 라떼를 만들 때, 한 잔의 바닐라 라떼마다 새로 레시피를 생성하지는 않는다.
>
> 미리 바닐라 라떼의 레시피를 정해두고, 그 레시피를 활용해 100잔 300잔의 커피를 만든다.
>
> 파이썬 OOP 세계에서는 이 레시피를 **클래스**라고 부른다.
>
> (개별 바닐라 라떼들은 **객체**이다. )



 ### 2-1. 📃 클래스 (Class)

> - 도면, 청사진(blueprint), 레시피
> - 사전에 정의해둔 속성과 메서드의 집합

```python
class 바닐라_라떼:
    '''
    바닐라 라떼 클래스입니다.
    '''
    # 바닐라 라떼 제조 대수 -> 바닐라 라떼 관련 '데이터'
    # (== 클래스 '속성')
    
    # 바닐라 라떼를 만들면 사용할 수 있는 '행위(기능)'
    # (== 인스턴스를 만들면 사용할 수 있는 '메서드')
    def drink(self):
        print('꼴깍 꼴깍 맛있다')
        
    def wake_up(self):
        print('잠이 홀딱 달아나네')
```



### 2-2. ☕ 인스턴스(Instance)

> - 도면을 토대로 만들어낸 실제 물건(Object, 객체)
> - 객체가 메모리에 할당되어 생성되는 순간 인스턴스가 된다.
>   - 바닐라 라떼 한 잔을 완성하고, 바닐라 라떼는 세상에 하나 밖에 없는 고유한 커피가 된다.
>   - 핸드폰의 경우, 휴대폰 조립을 완성하고, 휴대폰 안에 하나 밖에 없는 고유한 시리얼 번호가 생성되는 원리와 동일하다.



---

>  파이썬의 모든 것은 객체다. 객체는 클래스를 토대로 만들어진다.
>
> 클래스도 객체다. 클래스 객체는 무엇으로 만드는 거지..?! 🙄



**메타 클래스(meta Class)**

> : 클래스를 만드는 클래스 ( `<class 'type'>` )
>
> - `type`이라는 메타클래스는 재귀적으로 자신을 클래스로 삼게끔 설계되어 있다. 



```python
# class 생성
class VanilaLatte:
    count = 0
```

```python
# instance 생성
latte_for_milk = VanilaLatte()  
latte_for_dotou = VanilaLatte()

# instance의 type => class
print(type(latte_for_milk))
#=> <class 'VanilaLatte'>

# class의 type => type
print(type(VanilaLatte))
#=> <class 'type'>

# type의 type => type
print(type(type))
#=> <class 'type'>
```





### 2-3. 메서드(method) 정의

> 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위(behavior)들을 의미한다.



#### 2-3-1. `self`

> **`self`는 인스턴스 자신**을 의미한다.

- Python에서 인스턴스 메서드는 **호출 시 첫번째 인자로 인스턴스 자신이 전달**되게 설계되었다. <br> (인스턴스 메서드와 클래스 메서드의 차이는 다음 포스팅에서 자세히 다룰 예정이다!)
- 보통 매개변수명으로 `self`를 첫번째 파라미터로 설정하며, 다른 이름도 사용 가능하지만 추천하지 않는다! ~~예의상~~
- Java의 `this`와 비슷한 역할을 한다. - 본인 클래스를 반환

<br>

**활용법**

```python
# 1. 클래스 생성
class Person:
    # 2. 메서드 생성
    def talk(self):
        print('안녕?') 
       
	# 메서드도 function이기 때문에 추가적인 param을 받을 수 있다.
    def eat(self, food):
        print(f'{food} 냠냠')
```

```python
# 3. 인스턴스(객체) 생성
yewool = Person()

# 4. 인스턴스에서 메서드 사용
yewool.talk()        # '안녕?'
yewool.eat('볶음밥')  # '볶음밥 냠냠'
```

<br>



#### 2-3-2. 생성자 constructor 메서드 (`__init__`) 

> 인스턴스 객체가 생성될 때 호출되는 함수

- 생성자를 활용하면, 인스턴스가 생성될 때 **인스턴스의 속성을 정의**할 수 있다.
- 인스턴스의 **초기값** 설정(정의) 가능

**활용법**

```python
def __init__(self):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
```

<br>

#### 2-3-3. 소멸자 destructor 메서드  (`__del__`)

> 인스턴스 객체가 소멸되기 직전에 호출되는 함수

**활용법**

```python
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
```



😛 **생성자와 소멸자를 활용하여 클래스를 만들어보자!**

```python
class Person:
    
    def __init__(self, name, birthday):
        # __init__ 생성자에는 인스턴스의 속성을 할당해둘 수 있다.
        self.name = name # Java의 생성자에서 this 키워드와 동일한 방식으로 쓰인다.
        self.birthday = birthday
        print(f'응애 난 <{self.birthday}>에 태어난 아기 {self.name}')
        
    def __del__(self):
        print(f'안녕 세상아.. by {self.name}')
```

<br>

인스턴스를 생성해보자

```python
from datetime import datetime

yewool = Person('예울', datetime.today())
```

```
응애 난 <2021-01-27 21:37:51.047564>에 태어난 아기 예울
```



만든 인스턴스를 소멸시켜 보자.

```python
del yewool
```

```
안녕 세상아.. by 예울
```





---

## 3. 정리

**객체**

- `속성(attribute)`과 `행위(behavior)`로 이루어져 있다.

> **속성은?** 클래스/인스턴스가 가지는 값(데이터)
>
> **메서드는?** 클래스/인스턴스에 적용 가능한 조작법(method) **&** 클래스/인스턴스가 할 수 있는 행위(function)



**클래스 vs 인스턴스**

- 클래스 : 공통된 속성과 행위를 정의한 것으로, 객체지향 프로그램의 기본적인 **사용자 정의 데이터형**
- 인스턴스 : 특정 클래스로부터 생성된 해당 클래스의 실체/예시



<br>



추가 설명!

> 🙅‍♀️ `method`와 `function`은 무슨 차이일까?

클래스 안에 정의되어있는 function을 method라고 부른다!

즉, method ⊂ function 이다.

<br>

클래스 **바깥**에  정의한 function과 클래스 **안**에 정의한 function을 

용어적으로 구분하기 쉽게 하기 위해서 각 이름을 다르게 부른다!

