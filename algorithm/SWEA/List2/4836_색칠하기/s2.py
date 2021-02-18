import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):

    # 빈 리스트
    paper = [[0 for _ in range(10)] for _ in range(10)]


    print("#{} {}".format(tc, result))