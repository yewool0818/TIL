import sys

sys.stdin = open("input.txt")

# 최저 높이의 상자 인덱스 위치 반환
def min_search():
    # 초기화
    min_value = 987654321
    min_idx = -1

    for i in range(len(box)):
        if box[i] < min_value:
            min_value = box[i]
            min_idx = i

    return min_idx

# 최고 높이의 상자 인덱스 위치 반환
def max_search():
    # 초기화
    max_value = 0
    max_idx = -1

    for i in range(len(box)):
        if box[i] > max_value:
            max_value = box[i]
            max_idx = i

    return max_idx

T = 10
for tc in range(1, T + 1):
    # N = 덤프 횟수
    N = int(input())
    # 박스들
    box = list(map(int, input().split()))

    # N번 덤프하기
    for i in range(N):
        # 최고 높이 상자 한 칸 내리기
        box[min_search()] -= 1
        # 최저 높이 상자 한 칸 올리기
        box[max_search()] += 1

    print("#{} {}".format(tc, max(box)-min(box)))