import requests
from tmdb import URLMaker
from pprint import pprint

# B. 특정 조건에 맞는 영화 출력
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
