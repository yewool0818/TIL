import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N : 원소의 개수
    # M : 구간의 길이
    N, M = map(int, input().split())
    # nums : 정수 리스트
    nums = list(map(int, input().split()))

    min_value = 987654321
    max_value = 0

    # 중복 연산을 피해보자!

    # 첫 구간을 구해놓자
    tmp = 0
    for i in range(M):
        tmp += nums[i]

    max_value = tmp
    min_value = tmp

    # M번부터 N-1까지 구해보자
    for i in range(M, N):
        tmp = tmp + nums[i]  # 가장 뒤의 값 더하기
        tmp = tmp - nums[i - M]  # 가장 앞의 값 빼기

    print("#{} {}".format(tc, max_value - min_value))
