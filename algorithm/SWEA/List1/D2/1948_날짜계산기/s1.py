import sys

sys.stdin = open("input.txt")

T = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    d = d2 - d1 + 1
    ans = d
    for i in range(m1, m2):
        ans += days[i]

    print("#{} {}".format(tc, ans))