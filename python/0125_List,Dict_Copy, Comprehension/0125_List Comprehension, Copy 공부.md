# 21.01.25 Python 데이터 구조



## 1. 리스트



### 1-1. 리스트 복사

>🤔 mutable Collections vs immutable Collections 

| mutable Collections                                          | immutable Collections                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 변환이 가능한 자료구조                                       | 변환이 불가능한 자료구조                                     |
| 바꾸더라도 기존의 주소 값에서 수정된다.<br />같은 객체를 공유한다. | 바꿀 경우 새로운 주소값으로 할당된다.<br />같은 객체를 공유하지 않는다. |
| list, dictionary                                             | number, string, tuple                                        |



🤷‍♀️ 그렇다면 Mutable 데이터인 list를 복사할 때, 어떻게 해야할까?

> 파이썬에서 대입문(`=`)은 객체를 복사하지 않고, 대상과 객체 사이에 **바인딩**을 만듭니다.<br />
>
> 가변 (mutable) 컬렉션 또는 가변(mutable) 항목들을  포함한 컬렉션의 경우 때로 **원본 컬렉션을 변경하지 않고, 사본을 변경하기 위해 복사가 필요합니다.** 이 모듈은 일반적인 **얕은 복사**와 **깊은 복사** 연산을 제공합니다. 

[Python Docs - Copy](https://docs.python.org/ko/3/library/copy.html)





#### 1-1-1. 할당 (단순 복사)

> 메모리 상의 같은 객체를 바라보게 된다.

- 두 개의 변수 중 하나만 변경되어도, 나머지 하나도 함께 수정되는 현상이 발생한다.
  why? ___주소 값이 같기 때문___에 변경하면 같이 변경된다!

```python
list_a = [1, 2, 3]
list_b = list_a

print(list_a)  # [1, 2, 3]
print(list_b)  # [1, 2, 3]

list_b[0] = 5
print(list_a)  # [5, 2, 4]
print(list_b)  # [5, 2, 4]
```



#### 1-1-2. 얕은 복사(shallow copy)

> 새로운 리스트를 생성한다.

- 얕은 복사는 리스트 안의 리스트, <u>내부 리스트는 원본과 동일한 메모리 주소를 가리킨다.</u>
- **얕은 복사 세 가지 방법**
  1. 슬라이싱 : `list_b = list_a[:]`
  2. list() : `list_b = list(list_a)`
  3. copy 모듈 : `list_b = copy.copy(list_a)`



**[슬라이싱 예제]**

```python
list_a = [1, 2, 3]
list_b = list_a[:]

print(list_a) # [1, 2, 3]
print(list_b) # [1, 2, 3]

# 복사한 리스트의 요소 변경
list_b[0] = 5

print(list_a) # [1, 2, 3] - 기존 리스트는 변경되지 않음
print(list_b) # [5, 2, 3] - 복사한 후 변경한 리스트만 변경이 적용됨
```



**[이중 리스트 슬라이싱 예제]**

```python
list_c = [1, 2, [3, 4]]
list_d = list_c[:]

print(list_c[2][0])  # 3

# 중첩된 리스트 요소 변경
list_d[2][0] = 99

print(list_c) # [1, 2, [99, 4]] 
print(list_d) # [1, 2, [99, 4]]
# - 내부 리스트는 원본과 동일한 메모리 주소를 가지기 때문에, 같이 바뀌게 된다.
```

- 얕은 복사는 리스트 안의 리스트, 내부 리스트는 원본과 동일한 메모리 주소를 가리킨다.



#### 1-1-3. 깊은 복사 (deep copy)

- 새로운 리스트를 생성하고, 그 안에 있는 리스트들도 새롭게 생성한다.
- `import copy` 모듈을 통해, `copy.deepcopy([org_list])`를 이용하여 사용한다.

```python
import copy

list_a = [1, 2, [3, 4]]
list_b = copy.deepcopy(list_a) # 깊은 복사를 통해 list_a를 복사하여 list_b에 할당했다.

# 복사한 리스트의 내부요소 변경
list_b[2][0] = 99

print(list_a)  # [1, 2, [3, 4]]
print(list_b)  # [1, 2, [99, 4]]
# 원본은 건드리지 않고, 깊은 복사를 통해 복사된 리스트의 요소만 변경되었다!
```





### 1-2. List Comprehension 



👍 **사용 방법**

> [ `expression` for `변수` in `iterable` ]
>
> or
>
> [ `expression` for `변수` in `iterable` if `조건식` ]
>
> or
>
> [ `expression1` if `조건식` else `expression2`  for `변수` in `iterable` ]



#### 1-2-1. [연습] 피타고라스 정리

**반복문 활용**

```python
result = []

for i in range(1, 50):
    for j in range(1, 50): 
        for k in range(1, 50): 
            if i**2 + j**2 == k**2:
                result.append((i,j,k))
                
print(result)
```

```
[(3, 4, 5), (4, 3, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 6, 10), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 5, 13), (12, 9, 15), (12, 16, 20), (12, 35, 37), (15, 8, 17), (15, 20, 25), (15, 36, 39), (16, 12, 20), (16, 30, 34), (18, 24, 30), (20, 15, 25), (20, 21, 29), (21, 20, 29), (21, 28, 35), (24, 7, 25), (24, 10, 26), (24, 18, 30), (24, 32, 40), (27, 36, 45), (28, 21, 35), (30, 16, 34), (32, 24, 40), (35, 12, 37), (36, 15, 39), (36, 27, 45), (40, 9, 41)]
```

👀 오잉?!?! `(3, 4, 5)`와 `(4, 3, 5)`는 같은 값인데..

위의 코드로 돌리니 `i`와 `j`가 둘 다 1부터 49까지 반복해서 겹치는 값이 발생한다..



그래서 아래와 같은 코드로 이를 해결했다! 

```python
result = []

for i in range(1, 50):
    for j in range(i+1, 50): # i+1부터 구하면 겹치는 값을 제거할 수 있다.
        for k in range(j+1, 50): # k도 마찬가지이다.
            if i**2 + j**2 == k**2:
                result.append((i,j,k))
                
print(result)
```

```
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45)]
```

~~list comprehension공부하다가 반복문 공부중..ㅎㅎ~~



**List Comprehension 활용**

```python
result = [(i, j, k) for i in range(1, 50) 
              for j in range(i+1, 50)
                  for k in range(j+1, 50)
                      if i**2 + j**2 == k**2]

print(result)
```

```
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45)]
```

위와 같이 삼중(다중) for문도 리스트 컴프리헨션을 적용할 수 있다.

이 때 순서는 [ `표현식`   `가장 바깥 for문`   `그 다음 for문`  `가장 안쪽 for문`  `조건문`] 순이다.



#### 1-2-2. [연습] 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하세요.

**[입력 예시]**

```python
words = 'Life is too short, you need python!'
```

**[출력 예시]**

```
Lf s shrt, y nd pythn!
```



**반복문 활용**

```python
vowels = 'aeiou'
words = 'Life is too short, you need python!'

result = []

for word in words:
    #vowels을 리스트로 형변환하여, 요소 비교를 했다.
    if not word in list(vowels): 
        result.append(word)
        
print(''.join(result))
```

```
Lf s t shrt, y nd pythn!
```



**List Comprehension 활용**

```python
vowels = 'aeiou'
words = 'Life is too short, you need python!'

result = [word for word in words if not word in list(vowels)]

print(''.join(result))
```

```
Lf s t shrt, y nd pythn!
```



---





## 2. 딕셔너리



### 2-1. 딕셔너리 순회 (반복문 활용)

> dictionary에서 `for`를 활용하는 4가지 방법

1. dictionary 순회 (`key` 활용)

   ```python
   # dictionary는 for문으로 반복 시, 기본이 key로 돌아간다.
   for key in dict:
       print(key) # key
       print(dict[key], dict.get('key')) # value
   ```



2. `.keys()` 활용

   ```python
   for key in dict.keys():
       print(key) # key
       print(dict[key], dict.get('key')) #value
   ```

   

3. `.values()` 활용

   ```python
   for val in dict.values():
       # dictionary에서 value값으로 key 값을 찾을 수는 없다.
       print(val) # value
   ```

   

4. `.items()` 활용

   ```python
   for key, val in dict.items():
       print(key) # key
       print(val) # value
   ```





#### 2-1-1. 딕셔너리 구축하기 (counter)

> 리스트가 주어질 때, 각각의 요소의 개수를 value 값으로 갖는 딕셔너리를 만드세요.



**[출력 예시]**

{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}



**코드**

```python
book_titles =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

book_title_dict = {}

for book_title in book_titles:
    # 만약 key에 book_title이 이미 있다면,
    if book_title in book_title_dict.keys():
        # 해당 key에 해당하는 value 값을 1씩 증가시켜준다.
        book_title_dict[book_title] += 1
    # 없다면,
    else:
        # 만들어주고 1로 할당한다.
        book_title_dict[book_title] = 1
    
print(book_title_dict)
```

```
{'great': 2,
 'expectations': 1,
 'the': 2,
 'adventures': 2,
 'of': 2,
 'sherlock': 1,
 'holmes': 1,
 'gasby': 1,
 'hamlet': 1,
 'huckleberry': 1,
 'fin': 1}
```



😃 **더 간단한 코드!** - dictionary에서 value default를 활용한다!

```python
book_titles =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

book_title_dict = {}
# 단어들을 반복하면서
for book_title in book_titles:
    # book_title_dict의 book_title에 1씩 추가해준다.
    # 이 때, 해당 key에 대한 value가 있으면 가져오고, 없으면 0으로 설정한다.
    #  - 여기에 1을 더해주는 것!
    book_title_dict[book_title] = book_title_dict.get(book_title, 0) + 1
```



❗ 말 그대로 key point !!

> ```
> get(key[, default])
> ```

- key 가 딕셔너리에 있는 경우 key 에 대응하는 값을 돌려주고, 그렇지 않으면 default 를 돌려준다.





### 2-2. Dictionary Comprehension

> List에서 사용했듯이 Dictionary에서도 comprehension을 활용할 수 있다.



**활용법**

```python
{key:value for attribute in iterable}
```



**활용 예제**

```python
blood_types = {'A':40, 'B':11, 'AB':4, '0':45}

negative_blood_types = 
	{'-'+key:value for key, value in blood_types.items()}
  
print(negative_blood_types)
#{'-A': 40, '-B': 11, '-AB': 4, '-O': 45}
```





### 2-3. Dictionary Comprehension + 조건



**활용법**

```python
{key: value for attribute in iterable if 조건식}

{key: value1(T) if 조건식 else value2(F) for attribute in iterable}
```



**활용 예제**

> 1. 미세먼지 농도가 80 초과 지역만 뽑아보자!

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}

result = {
    location:dust for location, dust in dusts.items() 
       	if dust > 80
	}

print(result) # {'대전': 82, '중국': 200}
```



> 2. 미세먼지 농도가 **80초과는 나쁨**, **80이하는 보통**으로 하는 value를 가지도록 바꿔보자.

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}

result = {loc:'나쁨' if dust > 80 else '보통' 
          for loc, dust in dusts.items()}

print(result)
```

```
{'서울': '보통', '대전': '나쁨', '구미': '보통', '광주': '보통', '중국': '나쁨'}
```



> 3. elif 도 사용할 수 있다. (if else 열거)

```python
result = {key:'매우나쁨' if value > 150 else '나쁨' 
          	if value > 80 else '보통'
          	if value > 30 else '좋음'
          	for key, value in dusts.items()}

print(resut)
```

```
{'서울': '보통', '대전': '나쁨', '구미': '좋음', '광주': '보통', '중국': '매우나쁨'}
```

