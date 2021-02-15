import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
    N = int(input())

    # 누적 값 초기화
    result = 0
    
    # 반복
    for n in range(1, N+1):
        # 홀수면
        if n % 2:
            result += n
        # 짝수면
        else:
            result -= n

    print("#{} {}".format(tc, result))