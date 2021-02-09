import json
from pprint import pprint


def movie_info(movie, genres):

    ## > 장르 아이디에 일치하는 장르 이름 목록 구하기

    # 1. 입력받은 movie dictionary에서 id값 추출하여 변수에 할당
    genre_ids = movie['genre_ids']

    # 2. 장르 아이디를 장르 이름으로 변환한 값을 담을 리스트 초기화
    gerne_names = []

    # 3. genres 딕셔너리 순회(반복)
    for genre in genres: #{'id':18, 'name':'Crime'}
        # 4. 만약 movie_info의 genre_ids와 일치하는 장르의 아이디가 있을 경우
        if genre['id'] in genre_ids:  # if 18 in [18, 80] -> True
            # 4-1. gerne_names에 해당 genre['id']의 gerne['name']을 추가한다.
            gerne_names.append(genre['name']) # print(gerne_names) -> ['Crime']


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

    return movie_info_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))