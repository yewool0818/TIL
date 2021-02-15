import sys

sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T + 1):
    # N : 총 상자의 개수
    # Q : 상자의 번호를 바꿀 횟수
    N, Q = map(int, input().split())

    # 처음 박스 리스트 (N개)
    box = [0 for _ in range(N)]

    for i in range(Q):
        # L, R : 각 L부터 R번까지 박스번호를 바꿈
        L, R = map(int, input().split())
        # box의 번호를 L번부터 R번까지 i번으로 박스 번호를 바꿔준다.
        for j in range(L, R+1):
            box[j-1] = i+1

    # box를 한 줄 출력을 위해 문자열로 만들어주기
    box = ' '.join(map(str, box))

    print("#{} {}".format(tc, box))