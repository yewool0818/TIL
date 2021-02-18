import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N : 달팽이 리스트의 크기
    N = int(input())

    # 1. 달팽이 리스트를 담을 빈 리스트 만들기
    result = [[0] * N for _ in range(N)]
    print(result)
    # 현재 시작 좌표
    x = 0
    y = 0


    # 달팽이는 우->하->좌->상을 반복한다.
    # 우하좌상 이동 델타만들기
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 달팽이에 넣을 숫자
    n = 1
    # 우하좌상 방향
    i = 0

    # 2. 달팽이 리스트에 숫자 넣기
    while n < N**2: # n부터 n**2+1까지!

        result[x][y] = n

        # 내 다음 좌표
        x = x + dx[i] # 행
        y = y + dy[i] # 열

        # 모서리를 벗어나지 않을 때
        if 0 < x <= N or 0 < y <= N : # 비어있는지 아닌지 여부 체크 여기서
            # 비어있다면
            if result[y][x] == 0:
                # 리스트에 값 입력
                result[y][x] = n
                # 입력할 값 +1
                n += 1
            # 비어있지 않다면
            else:
                # 방향 전환 (i가 인덱스를 넘어가면 0으로 다시!)
                i = 0 if i > 2 else i+1
                # 실행 취소 

        # 모서리를 벗어날 때
        else:
            # 방향 전환 (i가 인덱스를 넘어가면 0으로 다시!)
            i = 0 if i > 2 else i + 1
            #실행 취소

    print("#{} {}".format(tc, result))
