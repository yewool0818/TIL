import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N : 정수의 개수
    # M : 구간의 개수
    N, M = map(int, input().split())

    # 정수 리스트
    numbers = list(map(int, input().split()))

    # 구간 내 최소 합, 최대 합
    min_sum = sum(numbers)
    max_sum = 0

    # numbers를 M만큼씩 잘라서 더해보자
    for i in range(N-M+1): # 총 정수 길이에서 구간의 길이 만큼 뺀거 까지만
        # 각 구간의 합 (0~M, 1~M+1 ..)
        party_sum = sum(numbers[i:i+M])

        # 만약 최소합보다 작으면 최소합에 할당
        if party_sum < min_sum:
            min_sum = party_sum

        # 최대합보다 크면 최대합에 할당
        if party_sum > max_sum:
            max_sum = party_sum

    # 구간 최대합 - 최소합
    result = max_sum - min_sum

    print("#{} {}".format(tc, result))
