import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 가로 세로 박스룸의 크기
    N = int(input())
    # 주어지는 박스룸의 구성 리스트
    room = list(map(int, input().split()))
    result = 0

    # 1. 각 column에서의 박스 높이보다 높거나 같은 것을 counting한다.
    # -> 높거나 같으면 그 밑으로 가질 못함
    # 높거나 같은 박스의 갯수가 밑에 쌓이기 때문에 counting 해야 함
    # 해당 column에서 가장 높이 쌓여있는 박스가 해당 column에서 가장 낙차가 클 수 밖에 없음
    for i in range(N):
        # 2. box에 하나도 안 쌓여있다면 continue
        if not room[i]:
            continue

        # 3. 현재 column의 다음 column부터 현재보다 높거나 같은 박스 높이를 가진 column의 수를 구한다.
        this_count = 0
        for j in range(i+1, N):
            if room[j] >= room[i]:
                this_count += 1

        # 4.

print(room)

