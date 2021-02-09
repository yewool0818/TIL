import json
from pprint import pprint


def movie_info(movie):

    # 0. 해당되는 key를 list에 담기
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']

    # 1. 새로운 dictionary를 담을 변수 선언
    movie_info_dict = {}

    # 2. key_list 요소에 해당하는 정보만 추출 (for문 이용)
    for key in key_list:
        # key = id
        # movie_info_dict['id'] = movie['id']
        movie_info_dict[key] = movie[key]

    # 3. 새롭게 재가공한 dictionary 반환
    return movie_info_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))