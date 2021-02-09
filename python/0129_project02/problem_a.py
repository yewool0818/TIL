import requests
from tmdb import URLMaker
from pprint import pprint

# A. 영화 개수 카운트 기능 구현

def popular_count():

    # 1. UMLMaker 클래스의 인스턴스 생성 (api_key를 argument로 입력)
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