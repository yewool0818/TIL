import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N : 정수의 개수
    N = int(input())
    # numbers : 정렬되지 않은 숫자들
    numbers = list(map(int, input().split()))

    # 버블 솔트로 정렬
    for i in range(N-1, -1, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    # 버블 솔트 결과
    # -> numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    # 맨 뒤에서 반절까지,
    # 맨 뒤 인덱스가 1번 인덱스로 오고,
    # 맨 뒤 인덱스-1번 인덱스가 3번인덱스로 오고... 반복
    for i in range(0, N, 2):
        # i번째 자리에 현재 리스트에서 맨 끝 요소 삽입
        numbers.insert(i, numbers[-1])
        numbers.pop(-1)         # 맨 끝 요소 삭제

    # 위 반복문 결과
    # -> numbers = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]

    print("#{} {}".format(tc, ' '.join(map(str, numbers[:10]))))