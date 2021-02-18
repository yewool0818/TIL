import sys

sys.stdin = open("input.txt")

def solution(str1, str2):
    # str1의 요소가 str2의 요소에 속한 경우 딕셔너리에 넣고, 카운팅하기
    count_dict = {}

    for s2 in str2:
        for s1 in str1:
            if s1 == s2:
                count_dict[s1] = count_dict.get(s1, 0) + 1
                break

    # count_dict의 value순으로 정렬
    sorted_count = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
    # => [('Y', 2), ('P', 1), ('V', 1), ('X', 1)] 이런식으로 정렬됨
    
    # 첫 번째 key의 값 가져오기
    return sorted_count[0][1]


T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    result = solution(str1, str2)

    print("#{} {}".format(tc, result))