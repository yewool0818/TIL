import sys
sys.stdin = open("input.txt")


# 버블 정렬
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 전체 테스트 케이스 수
T = int(input())


for tc in range(1, T+1):
    # N : 각 케이스의 양수들의 개수
    N = int(input())
    # numbers : 양수 리스트
    numbers = list(map(int, input().split()))

    # 1) 정렬 후 출력
    # bubble_sort(numbers)
#   # print('#{} {}'.format(tc, numbers[N-1] - numbers[0]))

    # 2) 반복 후 출력
    max_value = 0
    min_value = 987654321

    for i in range(N):
        # 최대값 갱신
        if max_value < numbers[i]:
            max_value = numbers[i]

        # 최소값 갱신
        if min_value > numbers[i]:
            min_value = numbers[i]

    print('#{} {}'.format(tc, max_value - min_value))
