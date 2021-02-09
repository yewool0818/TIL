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