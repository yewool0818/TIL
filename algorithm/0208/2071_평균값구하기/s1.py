import sys
sys.stdin = open('input.txt')

N = int(input())
for i in range(1, N+1):
    row = list(map(int, input().split()))
    # 각 줄을 다 합칠 total과 총 길이
    total, length = 0, 0
    for number in row:
        total += number
        length += 1
    print('#{} {}'.format(i, round(total/length)))