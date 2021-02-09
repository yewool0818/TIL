# PROJECT 02 (21.01.29)

[toc]

## 📘 **오늘의 프로젝트 주제**

>파이썬 API를 활용한 웹 데이터수집 II

💻 **프로젝트 실행환경**

> 개발 언어 : Python 3.8
>
> 필수 라이브러리 : requests
>
> 사용 데이터
>
> > 1. TMDB API (https://developers.themoviedb.org/3)
> > 2. 영화정보 API 서비스
> > 3. 영화 검색 API 서비스

👊 **프로젝트 목표**

1. **`Requests` 모듈**과 **API**를 활용하여 웹에 접근해,
2.  **`요청` 과 `응답`을 통해**  JSON 형태로 데이터를 받아온 후, 
3. python을 통해 필요한 데이터를 수집하고, 가공하는 것이다!

<br>

---

### 📗 공부한 내용

### [ WEB ]

#### 1-1. 서버와 클라이언트

> 서버와 클라이언트는 HTTP 규약에 따라 **요청**과 **응답**을 하며 통신한다.

클라이언트에서 `request`(요청)을 보내면 서버를 통해 `response`(응답)을 받는다!

<br>

**잠깐 ! HTTP????? 🙋‍♂️**

HTTP는 Hyper Text Transfer Protocol의 약자로, 

**인터넷에서 데이터를 주고받을 수 있는 프로토콜**이다.

**프로토콜**은 **규칙**이라고 생각하면 된다. 

이렇게 규칙을 정해두었기 때문에, 모든 프로그램이 이 규칙에 맞춰 개발해서 서로 정보를 교환할 수 있는 것이다!

<br>



#### 1-2. API

>  컴퓨터와 컴퓨터 간에 서로 통신하기 위한 약속, 규약이다.



#### 1-3. url을 파헤쳐보자

**예시 url**

```
https://api.thmoviedb.org
/3/movie/top_rated?
api_key=132kafjdskf3__..&
region=KR&
language=ko
```

위 url은 무슨말인지?

- `https` : http중 `s`, security가 적용된 프로토콜이다.

- `api.thmoviedb.org` : 접근하려는 웹의 도메인 주소이다

- `/3/movie/top_rated` : 웹에서 접근하려는 페이지의 상세 주소이다

- `?` : 이 이후로 클라이언트가 서버에게 requeset(요청)한 데이터가 나타난다.

  - **`?`을 기준**으로
    - **앞 : 요청을 어디로 보낼지**
    - **뒤 : 요청을 무엇을 담아서 보낼 지 (정보)**

- ```api_key=132kafjdskf3__..&
  api_key=132kafjdskf3__..&
  region=KR&
  language=ko
  ```

  - 마치 딕셔너리처럼 `key`=`value`로 요청을 보낸다.
  - `&`로 엮어서 데이터를 여러 개 보낼 수 있다.
  - `쿼리(query)`라고 불리기도 한다.



#### 1-4. `Requests` 모듈

> Python에서 웹에 요청 `requeset`를 보내줄 수 있는 모듈이다.

​	📖 [Ruquests 사용법](https://requests.readthedocs.io/en/latest/user/quickstart/)



> `Requests` 모듈 사용 순서

1. **모듈 인스톨 방법**

   ```python
   $pip install requests
   ```



2. **import**

   ```python
   import requests
   ```



3. **url을 통해 서버에  request(요청)하고 response(응답) 반환받기**

   ```python
   response = requests.get('url')
   ```

   - 여기서 `url`은 위 예시에서처럼 단순 도메인이 아닌 필요한 정보 요청까지 보낼 수 있다.
   - `response` 변수에는 ~~잘 접근이 됐을경우~~ `200` class의 인스턴스가 할당이 되고,<br>이를 통해, 웹에 요청된 데이터에 대한 응답 데이터를 반환받아 활용할 수 있다.



4. **response(응답) 받은 데이터를 텍스트로 확인하기**

   ```python
   response.text
   ```

   위 코드를 통해, 데이터를 확인할 수 있으며

   ```python
   type(response.text)
   ```

   를 통해 응답받은 데이터의 타입을 확인할 수 있다.



5.  **json 타입으로 들어온 데이터를 dictionary 타입으로 변환해서 받아올 수 있다.**

   ```python
   response_dict = response.json()
   ```



#### 1-5. API에 접근하는 기본 class 예제

```python
import requests

class URLMaker():
    # base_url 설정 - 클래스 변수 : 클래스 사용 내내 고정된 값 - 모든 클래스에서 공유 가능
    base_url = 'https://developers.themoviedb.org/3'

    # 생성자 - api_key를 인스턴스 변수로 초기화하여 생성
    def __init__(self, key):
        self.key = key

    # 인스턴스 메서드
    # url 반환 
    def get_url(self, category, feature, **kwargs): # param으로 가변인자로 받아온다. - query string방식 이용을 위해
        # - class 속성인 base_url에 접근
        # - category, feature는 인스턴스에 할당되어 있는 변수가 아닌
        #   함수의 인자 argument로 들어온 값이기 때문에 self.변수명 형태가 아니라
        #   인자값(아규먼트값)을 바로 사용한다.
        url = f'{URLMaker.base_url}/{category}/{feature}'

        # 인스턴스 생성 시, 인스턴스 변수로 저장된 api_key 값을 받아온다.
        url += f'?api_key={self.key}'
        
        # 가변인자로 받아온 값을 쿼리스트링 방식으로 url에 이어준다.
        for key, value in kwargs.items():
            url += f'&{key}={value}'

        return url

    # 인스턴스 메서드
    # 영화 제목을 입력받아 영화 아이디를 반환
    # - 요청으로 받을 응답에 영화정보 데이터(json)가 있을 것이고, 그 id를 반환해줄 것이다.
    def movie_id(self, title):

        # 인스턴스 메서드인 get_url() 호출 (self/movie는 영화제목을 받아 영화정보를 반환)
        # - title을 입력하면 해당 영화제목에 맞는 영화 정보 url을 반환해준다.
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        
        # 만들어진 url을 통해 서버에 요청해, 응답을 받아온다.
        response = requests.get(url)

        # 받아온 데이터를 json -> dict으로 변환해준다.
        movie_dict = response.json()

        # 만약 영화 제목에 해당하는 값이 있다면 
        if movie_dict.get('results'):
            # movie_dict에서 movie_id를 추출한다.
            result = movie_dict.get('results')[0].get('id')
            # 영화 제목에 해당하는 id 반환
            return result
        # 해당하는 값이 없다면, - result가 비어있다면
        else:
            return None  # None을 출력한다.
```



- api_key를 입력하여 URLMaker 인스턴스 생성

  ```python
  maker = URLMaker('[api_key]')
  ```

- `get_url` 테스트

  ```python
  print(maker.get_url('movie', 'popular', region='KR', language='ko'))
  ```

  > 출력

  ```
  https://developers.themoviedb.org/3/movie/popular?api_key=[api_key]&region=KR&language=ko
  ```

---

## 👩‍💻 본격 프로젝트 시작!



**요구사항**

> 커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 
>
> 전체 데이터 중 필요한 데이터를 크롤링 하는 과정을 진행합니다. 
>
> 아래 기술된 사항은 필수적으로 구현해야 하는 내용 입니다.



---

### ✨ 1. 첫 번째 미션! 



#### > 영화 개수 카운트 기능 구현 `problem_a.py`

>영화 개수를 출력합니다.
>
>완성된 기능은 향후 커뮤니티 서비스에서 제공되는 기능으로 사용됩니다.

**풀이 순서**

> 1. 제공된 `tmdb.py` 내에 있는 `URLMaker()`클래스의 인스턴스 객체 `urlMaker`를 생성한다. -  `UMLMaker` 클래스에서 `api_key`값을 클래스 변수로 할당해주었다.
> 2. `urlMaker`에서 `get_url()` 메서드를 통해,  `url`을 반환받는다.
> 3. `url`을 통해 서버에  request(요청)하고 response(응답) 반환받는다. <br>**(`requests`모듈 사용!)**
> 4. json형태로 response받은 값을 text로 변환 후, 파이썬에서 사용 할 수 있도록 dictionary 형태로 바꾸어 `movie_dict` 변수에 저장해준다.
> 5. 데이터 길이 확인

위 순서로 문제를 풀다보니, 데이터의 길이가 `4`로 나와서 뭔가 이상하다 싶었다.

그래서 `movie_dict`의 key값들을 살펴봤다.

```python
dict_keys(['page', 'results', 'total_pages', 'total_results'])
```

위 처럼 `page`, `results`, `total_pages`, `total_results` 총 4개로 구성되어 있었다.

문제에서 요구하는 것은 `results`의 개수를 묻는 것 같았다.

> 받아온 json 파일에서는 `page`는 한 페이지만 왔고, `total_pages`와 `total_results`는 넘어오지 않았기 때문이다.
>
> ```python
> print(movie_dict['page'])  # 1
> ```

그래서 `movie_dict`의 `results`값에 접근해서 그 길이를 구해보았다.



**코드**

```python
import requests
from tmdb import URLMaker
from pprint import pprint

# 1. 영화 개수 카운트 기능 구현

def popular_count():

    # 1. UMLMaker 클래스의 인스턴스 생성
    urlMaker = URLMaker()

    # 2. get_url()을 통해 url 반환받기
    url = urlMaker.get_url()

    # 3. url을 통해 서버에 요청해서 응답받기 (request module 사용)
    response = requests.get(url)
    #print(type(response)) # <class 'requests.models.Response'>

    # 4. 응답받은 json 타입 데이터를 dictionary 타입으로 바꿔서 변수에 저장
    #print(type(response.json()))  # <class 'dict'>
    movie_dict = response.json()
    
    # 5. 총 페이지 수 확인
    #print(movie_dict['page']) # 1

    # 6. movie_dict의 results를 추출해, 길이 반환
    return len(movie_dict['results'])
    


if __name__ == '__main__':
    print(popular_count())
```

<br>

**출력값**

```
20
```

<br>

총 20개의 영화 데이터가 있음을 확인할 수 있었다 !

<br>

참고로, `popular`를 기준으로 받아온 데이터이다! 

왱??  😮

`tmdb.py`의 `get_url`의 default 파라미터 값이 `movie`카테고리의 `popular`특징이기 때문에, 아무 입력값 없이 `get_url()`을 실행하면, `popular`기준의 영화 데이터가 온다!

---

### ✨ 2. 두 번째 미션! 



####  > 특정 조건에 맞는 영화 출력 `problem_b.py`

> popular를 기준으로 가져온 영화 목록 중
>
> **평점이 8 이상**인 영화 목록을 출력하는 기능을 완성합니다.

**풀이 순서**

> 1. `tmdb.py`패키지 내의 `UrlMaker()` 클래스의 `get_url()`메서드를 통해 `url`주소를 받아온다.
> 2. 받아온 `url`로 `requests` 모듈을 활용해, 데이터를 요청하고 응답값을 받아온다.
> 3. 응답받아온 데이터를 dictionary로 형변환한다. (`movie_dict`에 할당)
> 4. `movie_dict`에서 영화 데이터를 담고 있는  `results`를 리스트로 받아온다. (`movie_details`)
> 5. `movie_details`에서 `vote_average`요소에 접근해서, 평점이 8이상인 경우에 미리 정의해둔 리스트에 담는다.

`movie_details`는 list형태지만, 그 안에 딕셔너리 형태로 각 영화의 정보들이 있다.

반복문을 통해 각 영화 상세 정보에 접근할 수 있고, 

그 때 key값으로 `vote_average`를 주어 해당 값이 8 이상인지 비교할 수 있다.



**코드**

```python
import requests
from tmdb import URLMaker
from pprint import pprint

# 2. 특정 조건에 맞는 영화 출력
def vote_average_movies():
    # 0. 평점 8 이상인 영화 목록을 담는 리스트 초기화
    vote_average_movies_over_8 = []

    # 1. `tmdb.py`패키지 내의 `UrlMaker()` 클래스의 `get_url()`메서드를 통해 `url`주소를 받아온다.
    url = URLMaker().get_url()

    # 2. 받아온 `url`로 `requests` 모듈을 활용해, 데이터를 요청하고 응답값을 받아온다.
    response = requests.get(url)

    # 3. 응답받아온 데이터를 dictionary로 형변환한다. (`movie_dict`에 할당)
    movie_dict = response.json()
    
    # 4. `movie_dict`에서 영화 데이터를 담고 있는  `results`를 리스트로 받아온다. 
    movie_details = movie_dict.get('results', None)

    # 5. movie_details 반복
    for movie_detail in movie_details:
        # 6. 개별 영화들의 평점 확인
        vote_average = movie_detail.get('vote_average', None)
        # 7. 8점 이상인 경우 vote_average_movies_over_8에 해당 영화 정보를 담는다.
        if vote_average >= 8:
            vote_average_movies_over_8.append(movie_detail)
    
    # 8. 평점 8 이상인 영화들의 목록을 담은 리스트를 반환한다.
    return vote_average_movies_over_8



if __name__ == '__main__':
    pprint(vote_average_movies())    

```

<br>

**출력값**

```python
[{'adult': False,
  'backdrop_path': '/kf456ZqeC45XTvo6W9pW5clYKfQ.jpg',
  .. 중략 ..,
  'vote_average': 8.3,
  'vote_count': 4234},
 {'adult': False,
  'backdrop_path': '/yR27bZPIkNhpGEIP3jKV2EifTgo.jpg',
  .. 중략 ..,
  'vote_average': 8.5,
  'vote_count': 326}]

```



평점이 8 넘는 영화들이 2개가 있었다!

지금까지 문제는 저번 프로젝트에서 쓰인 `json()`과 딕셔너리와 리스트 반복문만 잘 공부했으면, 어렵지 않게 풀 수 있는 문제인 것 같다!



---

### ✨ 3. 세 번째 미션! 



####  > 평점 순 정렬 `problem_c.py`

> popular를 기준으로 가져온 영화 목록을 평점순으로 출력하는 함수를 완성합니다.
>
> 해당 기능은 향후 커뮤니티 서비스에서 기본으로 제공되는 영화 정보로 사용 됩니다.

**목표**

> **✍ 딕셔너리 내 하나의 key에 속하는 값을 기준으로 정렬**
>
> 받아온 데이터 중 평점이 높은 영화 다섯개의 정보를 리스트로 반환하는 함수 ranking을 완성합니다.

**풀이 순서**

>1. 두번째 미션과 동일한 순서로 영화 상세정보를 받아온다.
>2. 람다 표현식을 활용하여 movie_details의 `vote_average`순으로 정렬한다.
>3. 평점 값 내림차순으로 정렬된 딕셔너리 중 앞에 5개 정보를 추출하여, 반환한다.



리스트 안에 있는 딕셔너리들 중 하나의 key값을 기준으로 정렬하는 법이 뭘까..

고민해봤다.

평점 값을 하나하나 비교해가면서 리스트에 넣어갈까 생각했지만 그러기엔 좀 ~~귀찮고~~, 더 효율적인 방법이 있지 않을까 싶어 고민하다가 묵혀두었던 `람다 표현식`이 떠올랐다.

`람다 표현식`이란 쉽게 말해 함수를 한 줄로 표현하여 바로 적용하는 것으로 볼 수 있다.

다음과 같이 표현식을 사용하였다.

```python
sorted(movie_details, key=lambda x:x['vote_average'], reverse=True)
```

위 코드를 해석하면,

- `sorted(~~, reverse=True)` : 들어오는 리스트를 내림차순으로 정렬하겠다.
- `movie_details, key=lambda x:x['vote_average']`<br>: movies_details에 람다표현식을 적용하겠다.<br>: `x`에 sorted(~~, reverse=True)를 적용하는데, x는 movies_details['vote_average'] 하나 하나 값이다.



**나의 코드**

```python
import requests
from tmdb import URLMaker
from pprint import pprint

# C. 평점 순 정렬

def ranking():
    # 0. 평점이 높은 순으로 영화 정보를 다시 담을 리스트 정의
    vote_average_movies_top5 = []

    # 1. `tmdb.py`패키지 내의 `UrlMaker()` 클래스의 `get_url()`메서드를 통해 `url`주소를 받아온다.
    url = URLMaker().get_url()

    # 2. 받아온 `url`로 `requests` 모듈을 활용해, 데이터를 요청하고 응답값을 받아온다.
    response = requests.get(url)

    # 3. 응답받아온 데이터를 dictionary로 형변환한다. (`movie_dict`에 할당)
    movie_dict = response.json()
    
    # 4. `movie_dict`에서 영화 데이터를 담고 있는  `results`를 리스트로 받아온다. 
    movie_details = movie_dict.get('results', None)

    # 5. 람다 표현식을 활용하여 movie_details의 `vote_average`순으로 정렬된 딕셔너리를 리스트에 할당한다.
    sorted_movie_details_by_vote_avg = sorted(movie_details, key=lambda x: x['vote_average'], reverse=True)

    # 6. 정렬된 딕셔너리에서 앞에 5개 값만 가져오기
    vote_average_movies_top5 = sorted_movie_details_by_vote_avg[:5]

    # 7. 높은 평점 영화 5개 순으로 출력
    return vote_average_movies_top5


if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())
```

<br>

**출력값**

```python
[{'adult': False,
  .. 중략..,
  'vote_average': 8.5,
  'vote_count': 326},
 {'adult': False,
  .. 중략..,
  'vote_average': 8.3,
  'vote_count': 4234},
 {'adult': False,
  .. 중략..,
  'vote_average': 7.7,
  'vote_count': 1303},
 {'adult': False,
  .. 중략..,
  'vote_average': 7.3,
  'vote_count': 4144},
 {'adult': False,
   .. 중략..,
  'vote_average': 7.2,
  'vote_count': 59}]
```



이렇게 평점 탑 5가 나왔다.

그런데 사실 평점이 7.2인 영화가 두 개여서 top6로 할까 고민했지만..

음.. 문제의 요구사항을 따르기로 했다.



---

### ✨ 4. 네 번째 미션! 



####  > 제목 검색, 영화 추천 `problem_d.py`

> 해당영화를 기준으로 추천영화 목록을 출력하는 함수를 완성합니다. 
> 
>해당 기능은 향후 커뮤니티 서비스에서 추천영화 기능으로 사용됩니다.

**요구사항**

>1. 제공되는 tmdb.py를 이용하여,<br>영화 제목을 기준으로 TMDB에서 사용하 는 id를 검색합니다.
>2. id를 기준으로 추천영화 목록 조회 URL을 생성합니다.
>3. TMDB에서 추천받은 영화 리스트에서 제목을 리스트에 저장합니다.
>4. 저장된 리스트를 반환하는 함수 recommendation을 완성합니다.
>   * 올바르지 않은 영화 제목으로 id가 없는 경우 None을 반환합니다. 
>   * id값은 있지만 추천영화가 없는 경우 빈 리스트를 반환합니다.

음.. 어려워보인다. 풀이 순서 계획을 못짜겠다.

일단 위 요구 사항 순서대로 문제를 풀어보자!

<br>

추천 영화 목록을 불러오려면, API 부분에 `/movie/{movie_id}/recommendations`이 형식으로 호출해야한다.

그래서 UrlMaker 클래스의 인스턴스에서 `get_url()`을 할 때,  `feature`를 바꿔줘야한다.

`feature`에는 `movie_id()` 메서드를 통해  추출한 `movie_id`를 할당해주고, 그 뒤에 +하여 `/recommendations`를 추가해줘야겠다!



**나의 코드**

```python
import requests
from tmdb import URLMaker
from pprint import pprint

# D : 제목 검색, 영화 추천
def recommendation(title):

    # 1. 제공되는 tmdb.py를 이용하여,<br>영화 제목을 기준으로 TMDB에서 사용하는 id를 검색합니다.
    urlMaker = URLMaker()
    m_id = urlMaker.movie_id(title)

    # 2. id를 기준으로 추천영화 목록 조회 URL을 생성합니다.
    url = urlMaker.get_url(feature=f'{m_id}/recommendations', language='ko')

    # 3. TMDB에서 추천받은 영화 리스트에서 제목을 리스트에 저장합니다.
    movie_dict = requests.get(url).json().get('results', None)
    # * 올바르지 않은 영화 제목으로 id가 없는 경우 None을 반환합니다. 
    if movie_dict == None:
        return None
    
    # * id값은 있지만 추천영화가 없는 경우 빈 리스트를 반환합니다.
    recommend_movies = [movie.get('title') for movie in movie_dict]

    # 4. 저장된 리스트를 반환하는 함수 recommendation을 완성합니다.
    return recommend_movies


if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))    
    pprint(recommendation('id없는 영화'))
   
```

<br>

출력값

```python
['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃',
 '1917','조커','아이리시맨','미드소마','라이트하우스', '그린 북', '언컷 젬스',
 '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', '더 페이버릿: 여왕의 여자',
 '두 교황', '작은 아씨들','테넷','브레이킹 배드 무비: 엘 카미노']
[]
None
```

잘 나온다.

이번엔 `requests`모듈에서 `response`를 받은 후, `.json()`을 쓰지 않고,

바로 이어서 그 중 `results`값에 바로 접근해서 딕셔너리를 뽑아냈다.

점점 모듈 사용이 익숙해지고 있는 것 같다.

<br>

그나저나 `원스어폰어타임인 할리우드` 안봤는데 재밌나? 음.. 

추천 목록을 보니 기생충이 아카데미 수상한 작년 같이 후보에 있던 작품들을 추천해주는 것 같다.

그런데 왜 그래비티는 비슷한 추천영화가 없지? 인터스텔라, 마스 등등 많은데..

역시 영화 추천 서비스는 **왓챠가 최고다...**



---

### ✨ 5. 마지막 미션! 



####  > 배우, 감독 리스트 출력

> 영화에 출연한 배우들과 감독의 정보가 저장된 딕셔너리를 출력하는 함수를 완성합니다.
> 
>해당 기능은 향후 커뮤니티 서비스에서 기본으로 제공되는 영화 정보 로 사용됩니다.

**요구사항**

>1. 영화 제목을 기준으로 TMDB에서 사용하는 id를 검색합니다. 
>2. id를 기준으로 배우와 제작진 목록 조회 URL을 생성합니다. 
>3. requests 패키지를 이용하여 URL에 요청을 보냅니다.
>4. cast_id 값이 10보다 작은 배우의 이름을 리스트에 저장합니다. 
>5. department 값이 Directing인 감독의 이름을 리스트에 저장합니다. 
>6. 반환되는 딕셔너리는 cast, crew 두개의 key를 가지고 각각 배우리스트와 감독리스트를 value로 갖습니다. 
>7. 완성된 딕셔너리를 반환하는 함수 credits을 완성합니다

**풀이 순서**

> 1. UrlMaker 인스턴스 객체를 생성한다.
> 2. 앞에서 만든 함수에서처럼 입력된 영화명을 기준으로, 영화번호를 받아온다.
> 3. 이를 활용해서 배우, 감독 목록 조회 URL을 생성한다.
>    - 이때는 Get Credits를 통해 접근한다.<br>
>      (https://developers.themoviedb.org/3/movies/get-movie-credits)
>    - ``/movie/{movie_id}/credits`` 
> 4. 이 URL을 이용해서 requests 패키지를 이용해, json 데이터를 응답받아, dictionary 형태로 만들어준다.

여기까지 해보고 풀면서 요구사항을 적용해보자!



위 방법대로 응답받은 딕셔너리의 key값은

- 제대로 접근된 경우에는 `['id', 'cast', 'crew']`이고,
- 아닌 경우는 `['success', 'status_code', 'status_message']`이다.

이를 비교해서 **key값에 'success'가 있는 경우 None을 반환**해주도록 한다.



**코드**

```python
import requests
from tmdb import URLMaker
from pprint import pprint

def credits(title):
    # 0. 변수 초기화
    result_dict = {'cast':[], 'crew':[]}  # {cast:actors, crew:directors} 형태로 반환할 딕셔너리

    # 1. UrlMaker 인스턴스 객체를 생성한다.
    urlMaker = URLMaker()

    # 2. 입력받은 영화명을 기준으로, 영화번호를 받아온다.
    m_id = urlMaker.movie_id(title)

    # 3. 이를 활용해서 배우, 감독 목록 조회 URL을 생성한다.  -> /movie/{movie_id}/credits
    url = urlMaker.get_url(feature=f'{m_id}/credits')

    # 4. 이 URL을 이용해서 requests 패키지를 이용해, json 데이터를 응답받아, dictionary 형태로 만들어준다.
    people_dict = requests.get(url).json()

    # 5. 제대로 접근된 경우에는 key값이 ['id', 'cast', 'crew']이고,
    #    아닌 경우는 key값이 ['success', 'status_code', 'status_message']이다. 
    #    이를 비교해서 key값에 'success'가 있는 경우 None을 반환해주도록 한다.
    if 'success' in people_dict.keys():
        return None

    # 6-1. people_dict['cast']를 반복하며, 배우 상세정보 조회
    for actor in people_dict['cast']:
        # 6-2. cast_id 값이 10보다 작은 배우의 이름을 result_dict['cast']의 value값으로 추가한다.
        if actor['cast_id'] < 10:
            result_dict['cast'].append(actor['name'])

    # 7-1. people_dict['crew']를 반복하며, 스텝 상세정보 조회
    for crew in people_dict['crew']:
        # 7-2. department값이 Directing인 감독의 이름을 result_dict['crew']의 value값으로 추가한다.
        if crew['department'] == 'Directing':
            result_dict['crew'].append(crew['name'])

    # 8. 딕셔너리 값 반환
    return result_dict

if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('id없는 영화'))
```

<br>

**출력값**

  ```python
# credits('기생충') 결과값
{'cast': ['Song Kang-ho',
          'Lee Sun-kyun',
          'Cho Yeo-jeong',
          'Choi Woo-shik',
          'Park So-dam',
          'Lee Jung-eun',
          'Chang Hyae-jin'],
 'crew': ['Bong Joon-ho',
          'Han Jin-won',
          'Kim Seong-sik',
          'Lee Jung-hoon',
          'Park Hyun-cheol',
          'Yoon Young-woo']}

# credits('id가 없는 영화') 결과값
None
  ```



오.. 드디어 끝!

~~추가문제는 주말에 풀어봐야지~~



뿌듯한 하루가 되었다! 👧

---



## 👍 배운 점

> 이번 프로젝트에서 아래와 같은 것들을 배울 수 있었다!

- 람다 표현식이 늘 어렵다고 생각하고, 적용하지 않았는데, 적용해보니 정말 편하고 좋은 것 같다.<br>더 공부해서 자유자재로 써볼 수 있는 경지에 오르고 싶다.!
- 이제 `requests`모듈 사용이 익숙해졌다. 앞으로 배울 `selenium`이나 `beautifulsoup`도 이렇게 연습하다보면 익숙해지겠지? 기대된다.
- 웹에서 데이터를 받아오는 경우 json->dictionary해서 dictionary 형태로 받는 경우가 많은데, 이때 딕셔너리 안에 딕셔너리가 있어서 원하는 데이터가 어디있는지 찾기 어려운 경우가 많았다.<br>그럴 때, `.keys()`함수를 이용해서 딕셔너리를 구성하고 있는 key값들을 보고 접근하면 더 빠르고 정확하게 알 수 있다는 것을 배웠다. <br>앞으로 많이 활용해야지 ! 🧀