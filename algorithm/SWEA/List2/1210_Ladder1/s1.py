import sys

sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    tc = input()

    # data : 입력받은 사다리 2차 배열 리스트
    data = [list(map(int, input().split())) for _ in range(100)]

    # 하좌우(막혀있지 않은 경우) 조회하여 1인쪽으로 이동
    # 하 and 좌 or 우에 있는 경우 하 우선하여 이동

    # 델타 이동 (하, 좌, 우)
    dx = [0, -1, 1]
    dy = [1, 0, 0]



    print("#{} {}".format(tc, len(data)))