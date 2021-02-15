import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N : 달팽이 리스트의 크기
    N = int(input())

    # 1. 달팽이 리스트를 담을 빈 리스트 만들기
    result = [[0] * N for _ in range(N)]

    # 2. 달팽이 리스트에 숫자 넣기

    # 2-1. 홀수일 때
    if N % 2:
        # 원점은 N의 몫
        row, col = N//2, N//2

        # 원점까지 빙글빙글 숫자
        num = 1
        i = 0 # 행 index
        j = 0 # 열 index
        while num > N+1:
            if i > num:
                i -= 1
            if j > num:
                j -= 1

            result[i][j] = num

            i += 1
            j += 1
            num += 1


    # 2-2. 짝수일 때
    else:
        pass

    print("#{} {}".format(tc, result))
