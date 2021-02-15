import sys

sys.stdin = open("input.txt")

# 정수 자리 수만큼 잘라서 3, 6, 9 확인하기
def check(n):

    # 1. 자리 수 별로 자르기
    digit = 0
    cnt = 0

    while n: # n != 0
        digit = n % 10
        n //= 10

        # 2. 각 숫자가 3, 6, 9인지 확인 - 0일때 주의!
        if digit != 0 and digit % 3 == 0:
            cnt += 1

    return cnt


N = int(input())
for i in range(1, N+1):
    cnt = check(i)

    # 출력
    if cnt:
        for j in range(cnt):
            print("-", end="")
        print(" ", end="")
    else:
        print(i, end=" ")