import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N : N*N 행렬
    N = int(input())
    # matrix : 입력받은 N*N 행렬
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
    # 입력받은 행렬을 회전 후 입력할 빈 리스트
    results = [['']*N for _ in range(N)]
    # [['', '', ''],
    #  ['', '', ''],
    #  ['', '', '']]


    # 90도 회전
    for row in range(N):
        for col in range(N):
            spinned_row = N -(col+1)
            spinned_col = row
            results[row][0] += str(matrix[spinned_row][spinned_col])


    # 180도 회전
    for row in range(N):
        for col in range(N-1, -1, -1):
            spinned_row = N-row-1
            spinned_col = col
            results[row][1] += str(matrix[spinned_row][spinned_col])


    # 270도 회전
    for row in range(N):
        spinned_col = N-(row+1)
        for col in range(N):
            spinned_row = col
            results[row][2] += str(matrix[spinned_row][spinned_col])

    print("#{}".format(tc))
    for result in results:
        print(*result)