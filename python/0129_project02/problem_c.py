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