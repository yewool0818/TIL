# PROJECT 01 (21.01.22)





## 📘 **오늘의 프로젝트 주제**

>Python을 활용한 데이터 수집





### 📗 공부한 내용

### [ I/O (Input/Output) ]

#### 1-1. Input

**입력 함수 `open()`**

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

* encoding = `cp949`  : 윈도우의 인코딩방식 (주로 한글은 유니코드인 `utf8`을 사용한다.)



#### 1-2. JSON to dictionary

**JSON (JavaScript Object Notation)**

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



---



**요구사항**

> 커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 
> 전체 데이터 중 필요한 데이터를 추출해 나가는 과정을 진행합니다. 
> 아래 기술된 사항은 필수적으로 구현해야 하는 내용입니다



---

### ✨ 1. 첫 번째 미션! 



#### > 제공되는 영화 데이터의 주요내용 수집

:  json파일을 딕셔너리로 불러오는 함수가 이미 적혀있기 때문에 , 여기서 필요한 키워드만 골라 다시 새로운 딕셔너리로 반환해주는 함수를 만들어주면 된다.



처음에는 나름 머리를 써서 다음과 같이 코드를 짰다.

```python
import json
from pprint import pprint


def movie_info(movie):

    # 0. 해당되는 key를 list에 담기
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

    # 1. 새로운 dictionary를 담을 변수 선언
     movie_info_dict = ()

    # 2. key_list 요소에 해당하는 정보만 추출 (for문 이용)
     for key in key_list:
         movie_info_dict[key] = movie[key]

    # 3. 새롭게 재가공한 dictionary 반환
    return movie_info_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```



그런데.. **에러가 발생**했다 😂

```
TypeError: 'tuple' object does not support item assignment
```



```python
movie_info_dict[key] = movie[key]
```

for문 안에 있는 이 부분이 말썽을 부리는 것 같다.

'tuple' object는 item assignment를 지원하지 않는다고 한다.. 무슨 말인지 잘 모르겠어서 구글링을 해봤다.



깨달았다. 처음 딕셔너리 초기화 선언을 튜플로 해줬기 때문이다....~~허무하다~~



**최종 코드**

```python
import json
from pprint import pprint


def movie_info(movie):

    # 0. 해당되는 key를 list에 담기
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

    # 1. 새로운 dictionary를 담을 변수 선언
    movie_info_dict = {}

    # 2. key_list 요소에 해당하는 정보만 추출 (for문 이용)
    for key in key_list:
        movie_info_dict[key] = movie[key]

    # 3. 새롭게 재가공한 dictionary 반환
    return movie_info_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```



**결과값**

```
{'genre_ids': [18, 80],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```



잘 돌아간다. 만세! 🤗



이 방법(for문을 이용한 반복문) 외에도 딕셔너리 key를 직접 작성할 수 있다. 

이때 아래 꿀팁을 이용하면 매우 편리하다!

> 여러 줄을 반복해서 복사해야 하는 경우 `shift + alt + 방향키`를 누르면 편하다.



---

### ✨ 2. 두 번째 미션! 



####  > 제공되는 영화 데이터의 주요내용 수정

> 이전 단계에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔,
>
> 반환하는 함수를 완성합니다. 
>
> 완성된 함수는 다음 문제의 기본기능으로 사용됩니다.



**풀이 순서**

> 1. 앞에서 만든 함수 코드를 재활용한다. - 원하는 내용만 추출하여 새로운 딕셔너리 생성을 위해
>
> 2. 새로 가공된 딕셔너리에서 genre_ids값을 추출하여, 입력된 movie에서의 id와 비교하여,
>    
>    해당 딕셔너리의 key값이 'name'인 value값을 받아온다.

~~계획은 세웠지만, 어떻게 해야할지 모르겠다. 일단 코드를 짜보자!~~



**완성 코드**

```python
import json
from pprint import pprint


def movie_info(movie, genres):

    ## > 장르 아이디에 일치하는 장르 이름 목록 구하기
    # 1. 입력받은 movie dictionary에서 id값 추출하여 변수에 할당
    genre_ids = movie['genre_ids']   #[18, 80]

    # 2. 장르 아이디를 장르 이름으로 변환한 값을 담을 리스트 초기화
    gerne_names = []

    # 3. genres 딕셔너리 순회(반복)
    for genre in genres: #{'id':18, 'name':'Drama'}
        # 4. 만약 movie_info의 genre_ids와 일치하는 장르의 아이디가 있을 경우
        if genre['id'] in genre_ids: # if 18 in [18, 80] -> True
            # 4-1. gerne_names에 해당 genre['id']의 gerne['name']을 추가한다.
            gerne_names.append(genre['name']) 
            
    ## > 딕셔너리 값 재가공하기        
    # 5. dictionary에 넣을 key에 해당되는 요소를 list에 담기 (gerne_names 제외)
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']

    # 6. 새로운 dictionary를 담을 변수 선언
    movie_info_dict = {}

    # 2. key_list 요소에 해당하는 정보만 추출 (for문 이용)
    for key in key_list:
        movie_info_dict[key] = movie[key]

    # 장르 이름 추가
    movie_info_dict['gerne_names'] = gerne_names

    return movie_info_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```



**출력값**

```
{'gerne_names': ['Crime', 'Drama'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```



풀이를 계획했던 단계에서는 앞서 만든 재가공 함수코드를 이용해서, 딕셔너리를 이용하려고 했으나,

추후에 `gerne_ids` 요소를 빼고, 다시 `gerne_names`를 넣는 과정이 불필요하게 느껴졌다.

그래서 __풀이는 계획과 비슷하게 진행되었으나, 순서를 반대로 진행__하였다.



> 1.  장르 아이디에 일치하는 장르 이름 목록 구하기
> 2. 딕셔너리 값 재가공하기 
> 3. 재가공된 딕셔너리에 1.에서 진행항 `gerne_names`의 key, value 추가하기



페어 프로그래밍을 하며 짝에게 설명하면서 진행을 하니, 

내가 짰지만 완전히 로직을 이해하지 못했던 코드들을 한 줄 한 줄 잘 이해하면서 나아갈 수 있어 좋다!





---

### ✨ 3. 세 번째 미션! 



####  > 다중 데이터 분석 및 수정

> TMDB 기준 평점이 높은 20개의 영화데이터가 주어집니다. 
>
> 이 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성합니다.
>
> 완성된 함수는 향후 커뮤니티 서비스에서 제공되는 영화 목록을 제공하기 위한 기능으로 사용됩니다



앞에 문서와 **다른 점**은 **앞에서는 movie정보가 하나 들어왔다는 것이고, **
**이번 문제는 여러 개의 정보로 들어와서 리스트로 구성된다**는 점이다.



**풀이 순서**

> 1. movies를 for 반복문을 이용하여 movie로 하여, 앞에서 작성한 코드를 이용한다.
> 2. 새로 가공된 딕셔너리에서 genre_ids값을 추출하여, 입력된 movie에서의 id와 비교하여, 
>    해당 딕셔너리의 key값이 'name'인 value값을 받아온다.



**처음 코드**

```python
import json
from pprint import pprint


def movie_info(movies, genres):

    # movies : 영화 전체 정보
    # genres : 장르의 id, name 정보

    # 모든 영화 정보의 딕셔너리들을 리턴해줄 리스트를 선언한다.
    movies_info_dict = []

    ## > 장르 아이디에 일치하는 장르 이름 목록 구하기
    #    - 이 때, movies가 리스트로 들어오기 때문에 for문을 이용하여 반복문으로 구해준다.
    for movie in movies:
        # 1. 입력받은 movie dictionary에서 id값 추출하여 변수에 할당
        genre_ids = movie['genre_ids']

        # 2. 장르 아이디를 장르 이름으로 변환한 값을 담을 리스트 초기화
        gerne_names = []

        # 3. genres 딕셔너리 순회(반복)
        for genre in genres: 
            # 4. 만약 movie_info의 genre_ids와 일치하는 장르의 아이디가 있을 경우
            if genre['id'] in genre_ids:  # if 18 in [18, 80] -> True
                # 4-1. gerne_names에 해당 genre['id']의 gerne['name']을 추가한다.
                gerne_names.append(genre['name']) 


        ## > 딕셔너리 값 재가공하기 
        # 5. dictionary에 넣을 key에 해당되는 요소를 list에 담기 (gerne_names 제외)
        key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']

        # 6. 새로운 dictionary를 담을 변수 선언
        movie_info_dict = {}

        # 7. key_list 요소에 해당하는 정보만 추출 (for문 이용)
        for key in key_list:
            movie_info_dict[key] = movie[key]

        # 8. 장르 이름 추가
        movie_info_dict['gerne_names'] = gerne_names

    # 9. 재가공된 dictionary를 movies_info_dict에 추가해준다.
    movies_info_dict.append(movie_info_dict)

    # 10. 최종적으로 영화정보들이 담긴 리스트를 반환해준다.
    return movies_info_dict
        
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```



위와 같이 코드를 짜니,

결과가 마지막 영화의 dictionary만 결과가 나왔다. 

왜일까?😐

아하!😀

9번 주석쪽을 보면, movies_info_dict에 movie_info_dict를 append해준 것이 for문 밖에 있어서, 

**결론적으로 movies_info_dict에는**

**마지막에 movie_info_dict에 할당된 dictionary값만 append되었기 때문**이라는 것을 알 수 있다.



이를 수정해서 아래와 같이 **최종 코드**를 작성하였다.

```python
import json
from pprint import pprint


def movie_info(movies, genres):

    # movies : 영화 전체 정보
    # genres : 장르의 id, name 정보

    # 모든 영화 정보의 딕셔너리들을 리턴해줄 리스트를 선언한다.
    movies_info_dict = []

    ## > 장르 아이디에 일치하는 장르 이름 목록 구하기
    #    - 이 때, movies가 리스트로 들어오기 때문에 for문을 이용하여 반복문으로 구해준다.
    for movie in movies:
        # 1. 입력받은 movie dictionary에서 id값 추출하여 변수에 할당
        genre_ids = movie['genre_ids']

        # 2. 장르 아이디를 장르 이름으로 변환한 값을 담을 리스트 초기화
        gerne_names = []

        # 3. genres 딕셔너리 순회(반복)
        for genre in genres: 
            # 4. 만약 movie_info의 genre_ids와 일치하는 장르의 아이디가 있을 경우
            if genre['id'] in genre_ids:  # if 18 in [18, 80] -> True
                # 4-1. gerne_names에 해당 genre['id']의 gerne['name']을 추가한다.
                gerne_names.append(genre['name']) 


        ## > 딕셔너리 값 재가공하기 
        # 5. dictionary에 넣을 key에 해당되는 요소를 list에 담기 (gerne_names 제외)
        key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']

        # 6. 새로운 dictionary를 담을 변수 선언
        movie_info_dict = {}

        # 7. key_list 요소에 해당하는 정보만 추출 (for문 이용)
        for key in key_list:
            movie_info_dict[key] = movie[key]

        # 8. 장르 이름 추가
        movie_info_dict['gerne_names'] = gerne_names

        # 9. 재가공된 dictionary를 movies_info_dict에 추가해준다.
        movies_info_dict.append(movie_info_dict)

    # 10. 최종적으로 영화정보들이 담긴 리스트를 반환해준다.
    return movies_info_dict
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```



이렇게 하니 movies에 있는 모든 영화들이 재가공된 dictionary로 리스트에 잘 담겨 나왔다!

```
...생략...
 {'gerne_names': ['Comedy'],
  'id': 914,
  'overview': '세계대전에서 패배한 토매니아국에 힌켈이라는 독재자가 나타나 악명을 떨친다. 한편, 힌켈과 닮은꼴 외모의 이발사 '
              '찰리는 국가의 유태인 탄압정책으로 인해 곤경에 처하지만 병사로 참전했던 전쟁에서 우연히 구해줬던 슐츠 장교의 '
              '도움을 받아 위기를 모면한다. 독재자 힌켈의 악행은 갈수록 도를 더해가고, 찰리는 유태인 수용소에 끌려가게 되지만 '
              '기지를 부려 탈옥에 성공한다. 하지만 이발사와 똑같은 얼굴을 한 힌켈이 탈옥범으로 오해 받아 감옥에 잡혀 들어가게 '
              '되는데…',
  'poster_path': '/uw26mSTaA10hg2yuQfNaFLSeY3h.jpg',
  'title': '위대한 독재자',
  'vote_average': 8.4}]
```



완성 !  🍰





---

### ✨ 4. 네 번째 미션! 



####  > 알고리즘을 통한 데이터 출력

> 세부적인 영화 정보 중 수익 정보(revenue)를 이용하여,
> 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성합니다. 
>
> 해당 데이터는 향후 커뮤니티 서비스에서 메인 페이지 기본정보로 사용됩니다.



**목표**

> 수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue를 완성합 니다.



**풀이 순서**

> 1. 최대값을 구하기 위해, 관객수가 가장 높은 영화의 관객수와 영화 제목을 담을 변수를 초기화해준다.
> 2. for문을 이용해 movies를 각각의 movie로 뽑아 관객수를 초기화된 변수값과 비교한다.
> 3. 최대관객수를 구하고, 그에 해당하는 영화 제목을 변수값에 각 각 할당해준다.



**풀이 코드**

```python
import json
from pprint import pprint

def max_revenue(movies):
    pass
    # 여기에 코드를 작성합니다.  

    # 1. 변수 초기화
    max_revenue_value = 0  # 최다 수익
    max_revenue_title = '' # 최다 수익 창출 영화

    # 2. movies 순회(반복)하며, 최다 수익 영화 찾기
    for movie in movies:
        # 3. 해당 movie의 id를 이용해서 상세정보 파일 열기
        movie_detail = open("data/movies/"+str(movie['id'])+".json", encoding='UTF8') # json 파일 열기
        movie_detail_list = json.load(movie_detail)              # json to dictionary
        
        #  최다 수익 영화를 찾아 max_revenue_title에 해당 영화의 제목 할당
        if max_revenue_value < movie_detail_list['revenue']:
            max_revenue_value = movie_detail_list['revenue']
            max_revenue_title = movie_detail_list['title']

    return max_revenue_title
            
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
```



**출력값**

```
반지의 제왕: 왕의 귀환
```



이번 문제는 IO를 이용하여, 

​		1) json파일을 불러오고,

​		2) dictionary로 변환하여 활용하는

문제였다.



처음에 풀이 순서를 생각할 때는 그냥 movie dictionary에  `revenue`가 있을 줄 알았는데,
없어서 당황스러웠다.

문제를 다시 한 번 잘 읽어보니 `상세 파일`에 있다고 했고, 
`상세 파일`에 접근하는 방법은 movie['id']를 통해서 접근할 수 있었다.

아까 오전 수업 때, IO 수업을 열심히 들어서 어렵지 않게 해결할 수 있었다.



이번 문제의 key point는

> open(`path`) 함수를 이용하기 위해,  `path`를 정해 줘야 하는데, 
> 이 때, 적절한 `path`를 할당해주기 위해 movie['id']를 string으로 형변환해서 문자를 이어줘야한다.

인 것 같다!





---

### ✨ 5. 마지막 미션! 



####  > 알고리즘을 통한 데이터 출력

> `세부적인 영화 정보` 중 개봉일 정보(`release_date`)를 이용하여,
> 모든 영화 중 **12월에 개봉한 영화들의 제목 리스트를 출력**하는 알고리즘을 작성합니다. 
>
> 해당 데이터는 향후 커뮤니티 서비스에서 추천기능의 정보로 사용됩니다.



**목표**

>12월에 개봉한 영화 제목 리스트 출력!



**나의 코드**

```python
import json


def dec_movies(movies):
    # 1. 변수 초기화
    released_dec_movies_list = []

    # 2. movies 순회(반복)하며, 12월 개봉 영화 찾기
    for movie in movies:
        # 3. 해당 movie의 id를 이용해서 상세정보 파일 열기
        movie_detail = open("data/movies/"+str(movie['id'])+".json", encoding='UTF8') # json 파일 열기
        movie_detail_list = json.load(movie_detail)  # json to dictionary    

        # 4. '-'을 이용한 slicing을 통해 [1]번째 인덱스가 12인 영화의 제목 list에 담기
        release_date = movie_detail_list['release_date']
        if release_date.split('-')[1] == '12':
            released_dec_movies_list.append(movie_detail_list['title'])

    # 5. 12월 개봉작 반환
    return released_dec_movies_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
```



**출력값**

```
['그린 마일', '인생은 아름다워', '반지의 제왕: 왕의 귀환', '스파이더맨: 뉴 유니버스']
```



이번 문제는 앞 문제와 유사한 방법으로 풀면 됐었다.



이번 문제에서 내가 생각하는 key point는 !

> slicing이다 ! 



기존에 파이썬으로 데이터 분석을 하며 지겹게 slicing을 했던 게 많은 도움이 됐다..





---



## 👍 배운 점

> 이번 프로젝트에서 아래와 같은 것들을 배울 수 있었다!

- python의 IO ! json 파일을 불러오고, dictionary로 변환하는 법을 배울 수 있었다.
- 페어 프로그래밍을 통해,
  내가 짰지만 완전히 로직을 이해하지 못했던 코드들을 한 줄 한 줄 잘 이해하면서 나아갈 수 있어 좋다!
  더 많이 배울 수 있었다 !!