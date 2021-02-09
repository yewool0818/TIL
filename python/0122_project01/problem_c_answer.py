import json
from pprint import pprint
import problem_b_answer


def movie_info(movies, genres):

    # movies : 영화 전체 정보
    # genres : 장르의 id, name 정보

    # 모든 영화 정보의 딕셔너리들을 리턴해줄 리스트를 선언한다.
    movies_info_dict = []

    # movies가 리스트로 들어오기 때문에 for문을 이용하여 반복문으로 구해준다.
    for movie in movies:
        
        ## > 장르 아이디에 일치하는 장르 이름 목록 구하기
        
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