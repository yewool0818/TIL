import sys

sys.stdin = open("input.txt")

T = int(input())

def get_max(short, long):

    # 가장 큰 값으로 출력될 값을 초기화해준다.
    max_total = 0

    # 긴 것 덩어리 -  짧은 것 덩어리 + 1 번 반복해준다.
    # -> 긴 리스트 위로 짧은 리스트가 왼쪽부터 오른쪽으로 이동하는 것이다.
    for i in range(len(long) - len(short) + 1):
        total = 0
        # 짧은 리스트 길이만큼 긴 것과 짧은 것을 곱한 후, total에 더해준다.
        for j in range(len(short)):
            # 이 때 긴 리스트는 반복을 해줄 때 마다 한 인덱스씩 옆에 걸로 더해준다.
            tmp = long[i+j] * short[j]
            total += tmp

        # max_total과 비교해서 현재 total이 더 크면 재할당해준다.
        if max_total < total:
            max_total = total

    return max_total



for tc in range(1, T + 1):
    # N, M :각 숫자열의 길이
    N, M = map(int, input().split())
    # A, B : 각 N, M개의 숫자열
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # N, M을 비교해서 둘 중 작은 수를 함수의 첫번째 argument로 넣는다.
    if N <= M:
        result = get_max(A, B)
    else:
        result = get_max(B, A)

    print("#{} {}".format(tc, result))