# OOP (Inheritance 상속)

---

#### 목차

1. **상속** 
   1. `super()`
   2. [연습] Rectangle & Square
2. **메서드 오버라이딩 (Method Overriding)**
   1. 상속 관계에서의 namespace
      1. [연습] Pereson & Animal
3. **다중상속**

---



## 1. 상속 (Inheritance)

클래스의 가장 큰 특징은 `상속`이 가능하다는 점이다.

부모 클래스(super class)의 모든 멤버(속성, 메서드)이 자식 클래스(sub class)에게 상속되므로,

**코드 재사용성**이 높아진다.

<br>

**활용법**

```python
class ChildClass(ParentClass):
    <code block>
```



**부모 클래스와 자식 클래스 (상속)**

```python
# 부모 클래스
class Person:
    population = 0
    
    def __init__(self, name='사람'):
        self.name = name
        Person.population += 1
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
        
# 부모 클래스를 상속받은 자식 클래스
class Student(Person): # class 자식클래스(부모클래스)
    
    def __init__(self, name, student_id): # 생성자에 student_id가 추가됨
        self.name = name
        self.student_id = student_id
```



객체 생성 후, 자식 클래스의 기능을 확인해보자

```python
s1 = Student('박학생', '20210127')

print(s1.name)           # 박학생
print(s1.student_id)     # 20210127 => Student 클래스에 추가된 인스턴스 변수
```

물론 부모 클래스에 정의된 메서드 사용도 가능하다.

```python
s1.talk()  # 반갑습니다. 박학생입니다.
```



---

### 1-1. `super()`

위의 상속과정을 `super()`키워드를 통해 만들 수도 있다.

> 자식 클래스에 메서드를 추가로 구현할 수 있다.
>
> 부모 클래스의 내용을 사용하고자 할때, `super()`를 사용해서 부모 클래스를 가져올 수 있다.



**활용법**

```python
class ChildClass(ParentClass):
    
    def method(self, arg):   # 부모 클래스의 인스턴스 메서드 사용
        super().method(arg)  # 부모 클래스의 메서드 호출
```



**적용 예시**

```python
# super class
class Person:
    
    def __init__(self, name='사람'):
        self.name = name
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
        
# sub class        
class Student(Person):
    
    # Student 클래스를 생성할 때는 추가로 학번도 받고 싶을 때! - overriding해준다. 
    def __init__(self, name, student_id):
        super().__init__(name) # super class의 __init__메서드 호출 => 부모클래스의 init() 실행
        self.student_id = student_id
```

<br>

```python
# 부모 클래스의 객체들
p1 = Person('iu')
p2 = Person('jimin')

# 자식 클래스의 객체들 -> 생성 시 학번 추가 입력 가능 
s1 = Student('kim', '202101')
s2 = Student('park', '202102')
```

```python
s2.student_id         # '202102'
s2.talk()             # 반갑습니다. park입니다.
```

---

### 1-2. [연습] Rectangle & Square



1. **아래 조건에 만족하는 `Rentangle` 클래스를 생성해보자**

- 인스턴스 속성 

  - `length` : 가로 길이
  - `width` : 세로 길이

- 인스턴스 메서드

  - `area` : 직사각형의 넓이를 리턴한다.
  - `perimeter` : 직사각형의 둘레의 길이를 리턴한다.

  ```python
  class Rectangle():
      
      # 인스턴스 속성은 생성자에서 초기화해준다.
      def __init__(self, length, width):
          self.length = length
          self.width = width
          
      # 인스턴스 속성을 이용하기 때문에, param으로 self를 받는다.
      def area(self):
          # 인스턴스 속성을 이용한다.
          return self.length * self.width
      
      def perimeter(self):
          return 2 * (self.length + self.width)
  ```

  ​	

  **클래스 테스트!**

  - 인스턴스를 하나 만들어 가로 길이 4, 세로 길이 8인 직사각형의 넓이와 둘레 길이를 구해보자.

    ```python
    # 인스턴스 생성
    r1 = Rectangle(4, 8)
    
    # 넓이
    print(r1.area())        # 32
    
    # 둘레 길이
    print(r1.perimeter())   # 24
    ```



2. **`Rectangle` 클래스를 상속받아 `Sqaure` 클래스를 만들어 보자.**

   - `Square`클래스는 `Rectangle`클래스의 상속받은 속성 외 추가 속성은 없다.

   ```python
   class Sqaure(Rectangle):
       
       # 부모 클래스의 인스턴스 속성을 상속받아 사용하기 위해 
       # 초기화에서 super()를 통해 부모 클래스를 호출해서
       # 그 안에 __init__메서드를 호출한다.
       
       # + super() = Rectangle class의 인스턴스 변수이기 때문에
       # self = Sqaure 인스턴스 변수로 호출해줄 필요가 없다.
       def __init__(self, length, width):
           super().__init__(length, width)
   ```

   

   **상속 클래스 테스트**

   - Square 클래스로부터 인스턴스를 하나 만들어 가로/세로 길이4가 4인 직사각형의 넓이와 둘레 길이를 구해보자~

   ```python
   # Square 인스턴스 생성
   s1 = Sqaure(4, 4)
   
   # 넓이
   print(s1.area())      # 16
   
   # 둘레 길이
   print(s1.perimeter()) # 16
   ```

---

## 2. 메서드 오버라이딩

> **`Method Overriding` (메서드 재정의)**
>
> : 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것

* 상속 받은 메서드를 `재정의`할 수도 있다. 
* 상속 받은 클래스에서 **같은 이름의 메서드**로 덮어쓴다.



> 연습

- 부모 클래스인 Person 클래스를 만든다. 

  - 인스턴스 속성 : `name`, `age`, `number`, `email`
  - 인스턴스 메서드 : `talk()`

  ```python
  class Person:
      def __init__(self, name, age, number, email):
          self.name = name
          self.age = age
          self.number = number
          self.email = email
          
      def talk(self):
          print(f'안녕? 나는 {self.name}!')
  ```

- Person 클래스의 상속을 받아 군인처럼 말하는 Soldier 클래스를 만든다.

  - 이때 자식 클래스인 Soldier 클래스에 맞게 메서드를 재정의해보자. <br>:`method overriding`

  ```python
  class Soldier(Person):
      
      # 인스턴스 속성을 부모 클래스의 인스턴스 속성을 그대로 가져온다.
      # 파라미터에 self를 넣는 것은 Soldier 인스턴스에서 다음과 같은 속성들을
      # Soldier의 인스턴스 속성으로 사용하겠다는 의미이다.
      def __init__(self, name, age, number, email, level):
          super().__init__(name, age, number, email)
          self.level = level
          
      # 부모 클래스의 talk() 메서드를 군인스럽게 바꾸기 위해
      # method overriding을 한다.
      def talk(self):
          supe().talk() # 부모의 메서드 호출 - super()는 부모 클래스(인스턴스) 자체이다!
          if self.level == '참모총장':
              print("내 밑으로 집합")
          else:
              print(f'충성! {self.name}')
  ```

- 테스트 해보자

  ```python
  p = Person('일반인', 10, '010123', '1banin@gmail.com')
  p.talk()
  ```

  ```
  안녕? 나는 일반인!
  ```

  

  ```python
  goodgun2 = Soldier('굳건이', 25, '010123456', 'goodgun2@rok.kr', '이병')
  goodgun2.talk()
  ```

  ```
  안녕, 굳건이
  충성! 이병 굳건이입니다!
  ```

  

  ```python
  star = Soldier('4스타', 50, '010342123', 'zzang@rok.kr', '참모총장')
  star.talk()
  ```

  ```
  안녕, 4스타
  내 밑으로 집합.
  ```



> **🙅‍♀️ 헷갈리지 마세요!**
>
> - **overriding** : 부모 클래스의 멤버(속성, 메서드)를 상속받은 자식 클래스에서 본인에 맞게 재정의하여 사용하는 것
> - **overloading** : 같은 이름의 메서드를 parameter를 다르게 해주어, 다양한 매개변수를 받을 수 있어 활용도를 높이는 것!



### 2-1. 상속 관계에서의 이름공간(namespace)

- 기존의 `인스턴스 -> 클래스` 순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장된다.
- 인스턴스 -> 클래스 -> 전역
- 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역



#### 2-2-1. [연습] Person & Animal

> 사실 사람은 포유류입니다.
>
> Animal Class를 만들고, Person Class 가 상속받도록 구성해봅시다.
>
> (변수나, 메서드는 자유롭게 만들어보세요.)

```python
# 1. Animal class 생성
class Animal():
    # 인스턴스 메서드 - 파라미터값으로 self 필수! : 생성자도 예외없다..
    def __init__(self, species, age):
        self.species = species
        self.age = age
        
    # 인스턴스 메서드 - 파라미터값으로 self 필수!
    def walk(self):
        print(f"{self.species} 총총총")
       
    # 인스턴스 메서드 - 파라미터값으로 self 필수! 
    # (인스턴스 속성을 안 쓸지라도 인스턴스 메서드를 사용하는 거니까!)
    def eat(self):
        print('와구 와구')
        
        
# 2. Person class 생성 - Animal class 상속받기
class Person(Animal):
    
    # 세 개의 인스턴스 모두 오버라이딩하여,
    # 부모(Animal) 클래스의 메서드를 
    # 자식(Person) 클래스에 맞게 수정했다.
    
    # 생성자 - 인스턴스 메서드
    def __init__(self, species, age, name):
        # Animal 클래스(부모)의 인스턴스 속성을 받아와서
        # Person 클래스(자식)의 인스턴스 속성으로 할당한다.
        super().__init__(species, age)
        self.name = name
        
    # 인스턴스 메서드 - 파라미터 값으로 self 필수!
    def walk(self):
        print(f'{self.species} {self.name}, 뚜벅뚜벅')
        
    # 인스턴스 메서드 - 파라미터 값으로 self 필수!
    # (인스턴스 속성을 언 쓸 지라도 인스턴스 메서드를 사용하는거니까!)
    def eat(self):
        print('오물 오물')
```

테스트

```python
# Animal 인스턴스
a1 = Animal('강아지', 3)
a1.walk()   # 강아지 총총총
a1.eat()    # 와구 와구

# Person 인스턴스
p1 = Person('인간', 28, '예울')
p1.walk()    # 인간 예울, 뚜벅뚜벅
p1.eat()     # 오물 오물
```





## 3. 다중 상속 (Mulitple Inheritance)

> 두개 이상의 클래스를 상속받는 경우, 다중 상속이 된다.



1. Person(부모) 클래스를 정의한다.

2. Person 클래스를 상속받는 Mom, Dad(자식) 클래스를 정의한다.

   ```python
   # Person 클래스를 정의합니다.
   class Person:
       
       def __init__(self, name):
           self.name = name
           
       def talk(self):
           print('사람입니다.')
           
   # Mom 클래스를 정의합니다.
   class Mom(Person):
       # 클래스 변수
       gene = 'XX'
       
       def swim(self):
           print('첨벙 첨벙')
           
           
   # Dad 클래스를 정의합니다.
   class Dad(Person):
       # 클래스 변수
       gene = 'XY'
       
       def walk(self):
           print('씩씩하게 걷기')
   ```

   **테스트**

   ```python
   mommy = Mom('박엄마')
   mommy.swim()   # 첨벙 첨벙
   mommy.gene     # 'XX'
   mommy,talk()   # 사람입니다.
   ```

   ```python
   daddy = Dad('이아빠')
   daddy.walk()   # 씩씩하게 걷기
   daddy.gene     # 'XY'
   daddy,talk()   # 사람입니다.
   ```



3. Mom과 Dad 클래스를 다시 상속받을 FirstChild와 SecondChild 클래스를 정의한다.

   ```python
   # FirstChild 클래스를 정의합니다.
   class FirstChild(Mom, Dad):
       
       def cry(self):
           print('응애 응애')
           
       # super class의 walk를 overriding해줌
       def walk(self):
           print('아장 아장')
   ```

   **테스트**

   ```python
   baby = FirstChild('이아가')
   
   baby.cry()   # 응애 응애
   baby.swim()  # 첨벙 첨벙
   
   baby.walk()  # 아장아장
   
   baby.gene    # 'XX'
   ```

   - Mom과 Dad 클래스 둘 다의 메서드를 상속받아 사용한다.
   - `walk()`메서드도 오버라이딩한 것이 잘 적용된다.
   - 단, 둘 중 상속 인자로 앞에 쓴 값으로 클래스 속성을 상속받는다.

   

   **그렇다면 상속 순서를 바꿔보자**

   ```python
   # SecondChild 클래스를 정의합니다.
   class SecondChild(Dad, Mom):
       
       def cry(self):
           print('으아아아아아앙!')
   ```

   **테스트**

   ```python
   baby2 = SecondChild('이애기')
   
   baby2.cry()    # 으아아아앙! - 메서드 오버라이딩한 것 잘 적용
   baby2.walk()   # 씩씩하게 걷기 
   baby2.swim()   # 첨벙첨벙
   			   # - 별도로 자식클래스에서 메서드 오버라이딩을 하지 않아
       		   # 부모 클래스에서 정의된 내용 그대로 실행
           
   baby2.gene	   # 'XY'
   ```

   - 이번엔 클래스 정의 시, Dad -> Mom순으로 상속 파라미터를 적어주었기 때문에, Dad의 class 속성을 상속 받아왔다.

   

   **🙂 정리!**

   > **메서드 실행 방식 순서**
   >
   > 본인 클래스 → 부모 중 첫번째 정의된 클래스 → 부모 중 그 다음으로 정의된 클래스 → ...



