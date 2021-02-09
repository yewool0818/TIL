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
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
