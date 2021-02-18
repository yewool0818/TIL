import sys

sys.stdin = open("input.txt")

T = 10

for _ in range(1, T + 1):
    tc = int(input())
    # 0. 최댓값 초기화
    result = 0

    # 1. 배열 입력받기
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    row = len(arr)    # 행 길이
    col = len(arr[0]) # 열 길이
    
    # 2. 각 행의 합 중 최댓값 구하기
    for r in range(row): # 한 행 씩 반복
        sum_row = sum(arr[r]) # 해당 행의 합
        if result < sum_row:
            result = sum_row
    
    # 3. 각 열의 합 중 최댓값 구하기
    # 열 순으로 조회하여 각 열 더하기
    for r in range(row):
        col_sum = 0  # 새로 행마다 열 합 초기화
        for c in range(col):
            col_sum += arr[c][r]
        if result < col_sum:
            result = col_sum

    # 4. 대각선의 합 중 최댓값 구하기

    # 4-1. \ 모양 대각선
    cross_sum1 = 0
    r = 0
    c = 0
    while r < row and c < col:
        cross_sum1 += arr[r][c]
        r += 1
        c += 1

    if result < cross_sum1:
        result = cross_sum1

    # 4-2. / 모양 대각선
    cross_sum2 = 0
    r = 0
    c = col-1
    while r < row and c > -1:
        cross_sum2 += arr[r][c]
        r += 1
        c -= 1

    if result < cross_sum2:
        result = cross_sum2


    print("#{} {}".format(tc, result))