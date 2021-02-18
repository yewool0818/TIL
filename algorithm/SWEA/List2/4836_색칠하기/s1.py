import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 결과값 초기화 (색이 겹친 부분의 개수)
    result = 0

    # 색이 칠해질 격자 (2차원 빈 배열 리스트)
    paper = [[0]*10 for _ in range(10)]

    # N : 색칠을 칠할 영역의 개수
    N = int(input())

    # N번 영역이 지정되고, 색이 칠해짐
    for _ in range(N):
        # 칠할 영역 및 색
        r1, c1, r2, c2, color = map(int, input().split())

        # 빈 격자에 각 색 채우기
        # 행 채우기
        for r in range(r1, r2+1):
            # 열 채우기
            for c in range(c1, c2+1):
                paper[r][c] += color

    # 모든 색이 칠해진 후 3인 부분은 빨강(1) + 파랑(2) 이 겹친 부분이다
    # 이 부분의 개수를 출력하자
    for row in range(len(paper)):
        for col in range(len(paper)):
            if paper[row][col] == 3:
                result += 1

    print("#{} {}".format(tc, result))
