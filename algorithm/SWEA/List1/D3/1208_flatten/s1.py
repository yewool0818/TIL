import sys

sys.stdin = open("input.txt")

T = 10


def flatten(dump, boxs):
    # dump가 0이 될때까지 반복할 수 있다.
    while dump > 0:
        # 가장 높은 박스 위치와 가장 낮은 위치 조회
        highest = 0
        highest_idx = 0
        lowest = 100
        lowest_idx = 0

        for i, box in enumerate(boxs):
            if box > highest:
                highest = box
                highest_idx = i
            if box < lowest:
                lowest = box
                lowest_idx = i

        # 가장 높은 박스 -1, 가장 낮은 박스 +1 해주기
        boxs[highest_idx] -= 1
        boxs[lowest_idx] += 1

        dump -= 1

    # dump다 된 후 최종 가장 높은 위치-낮은 위치 뽑기
    return max(boxs) - min(boxs)


for tc in range(1, T + 1):
    # 총 덤프(높은 곳->낮은 곳 이동) 제한 횟수
    dump = int(input())
    # 박스 높이 리스트
    boxs = list(map(int, input().split()))

    result = flatten(dump, boxs)
    print("#{} {}".format(tc, result))


