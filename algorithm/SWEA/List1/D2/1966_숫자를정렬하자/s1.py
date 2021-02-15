import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 각 테이스 케이스 별 숫자의 개수
    N = int(input())
    # 정렬 대상 숫자 리스트
    numbers = list(map(int, input().split()))

    # 버블 정렬로 정렬해보자!
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    # 결과값을 하나의 문자열로 만들어주기 위해 numbers요소들을 str으로 변환 후 join해준다.
    result = ' '.join(map(str, numbers))

    # 출력
    print('#{} {}'.format(tc, result))
