# import sys

# sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N : 소인수분해 대상
    N = int(input())

    # primes : 소인수분해 계수
    primes = [2, 3, 5, 7, 11]

    # results : 소인수분해 지수
    results = [0] * 5

    # 주어진 소수의 수만큼 반복
    for i in range(len(primes)):
        # 대상인 정수가 계수(prime number)로 나누어 떨어지는 경우 반복해서 실행
        while N % primes[i] == 0:
            results[i] += 1
            N //= primes[i]

    print("#{} {}".format(tc, " ".join(map(str, results))))