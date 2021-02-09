import json
from pprint import pprint

def max_revenue(movies):

    # 1. 변수 초기화
    max_revenue_value = 0  # 최다 수익
    max_revenue_title = '' # 최다 수익 창출 영화

    # 2. movies 순회(반복)하며, 최다 수익 영화 찾기
    for movie in movies:
        # 3. 해당 movie의 id를 이용해서 상세정보 파일 열기
        movie_detail = open("data/movies/"+str(movie['id'])+".json", encoding='UTF8') # json 파일 열기
        movie_detail_list = json.load(movie_detail)                                   # json to dictionary
        
        #  최다 수익 영화를 찾아 max_revenue_title에 해당 영화의 제목 할당
        if max_revenue_value < movie_detail_list['revenue']:
            max_revenue_value = movie_detail_list['revenue']
            max_revenue_title = movie_detail_list['title']

    return max_revenue_title

 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))