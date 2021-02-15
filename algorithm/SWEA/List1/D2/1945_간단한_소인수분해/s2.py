import sys

sys.stdin = open("input.txt")

T = int(input())
primes = [2, 3, 5, 7, 11]

for tc in range(1, T + 1):
    # N : 소인수분해 대상
    N = int(input())

    # 결과를 담을 빈 리스트 초기화
    result = [0 for _ in range(len(primes))]

    # N이 더 이상 나누어 떨이지지 앟는 1이 되는 동안 계속 반복한다.
    i = 0
    while N != 1:
        # N을 소수로 나누며 나누어 떨어지는 경우,
        if not N % primes[i]:
            # 해당 인덱스에 1을 더해준다.
            result[i] += 1
            N //= primes[i]
        # 나누어 떨어지지 않는 경우 그냥 다음 소수로 넘어간다.
        else:
            i += 1

    print("#{}".format(tc), end=" ")
    for r in result:
        print(r, end=" ")
    print("")