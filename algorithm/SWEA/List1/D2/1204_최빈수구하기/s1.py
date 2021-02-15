import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # scores : 학생 1000명의 점수 리스트
    # scores의 각 원소는 0 이상 100 이하의 정수
    scores = list(map(int, input().split()))

    # 0~100점까지 각 점수의 빈 리스트
    freq_list = [0 for _ in range(101)]

    # 카운팅 : 각 점수에 해당하는 scores에 1씩 추가
    for i in range(len(scores)): #0, 1, 2, 3, .. , 100
        freq_list[scores[i]] += 1 #scores[0], scores[1] .., scores[100]

    # for score in scores:
    #     freq_list[score] += 1

    # 가장 높은 빈도의 수
    freq_idx = 0               # 최대 인덱스
    freq_value = freq_list[0]  # 최대갓

    for i in range(len(freq_list)):
        if freq_list[i] >= freq_value:
            freq_value = freq_list[i]
            freq_idx = i

    print("#{} {}".format(tc, freq_idx))
