> 요구사항

- 음악차트 페이지를 구성하기 위하여, 테이터를 수집하는 단계이다.



## 1. I/O (Input/Output)

### 1-1. Input

**입력 함수 `open()`**

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

* encoding = '`cp949` ' : 윈도우의 인코딩방식 (주로 한글은 유니코드인 `utf8`을 사용한다.)



### 1-2. JSON to dictionary

#### * JSON (JavaScript Object Notation)

> 데이터를 구조화하기 위한 구조체 
>
> (파이썬에서는 딕셔너리형태와 유사하다.)

```python
import json

# object를 json형태로 직렬화
json_obj = json.dump([dictionary])

# json을 python object로 변환
dict_obj = json.load([json])

```

