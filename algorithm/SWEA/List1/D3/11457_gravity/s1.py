import sys
sys.stdin = open("input.txt")

T = int(input())

N = int(input())

def gravity_check(numbers):
    result = 0

    # 각 row 별 빈 리스트를 채우자
    box_room = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for i in range(numbers[row]):
            box_room[row][i] += 1

    for box in box_room:
        print(box)

    # 각 column에서 1인 것 끼리 row 차이를 비교해보자 -- 못하겠따 ㅠㅠ
    for col in range(N):
        for row in range(N):
            if box_room[row][col] == 1:
                pass

    return result

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    result = gravity_check(numbers)
    print("#{} {}".format(tc, result))


