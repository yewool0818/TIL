import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    # 총 정수의 개수
    N = int(input())

    # 입력된 정수 리스트로 변환
    numbers = list(map(int, input().split()))

    # 최댓값과 최솟값을 초기화해준다.
    # 이 때 정수 리스트의 맨 앞 값을 기준으로 잡아주어 다른 것들과 비교 가능하도록 한다.
    max_number = numbers[0]
    min_number = numbers[0]

    # numbers 순회
    for number in numbers:
        # 만약 할당된 최소값보다 현재 number가 작다면 최소값으로 할당
        if number < min_number:
            min_number = number
            continue # 이 조건을 충족했더라도 최댓값을 구해야하니까 밑에 if 실행

        # 만약 할당된 최소값보다 현재 number가 크다면 최댓값으로 할당
        if number > max_number:
            max_number = number

    # 가장 큰 수와 가장 작은 수의 차이
    result = max_number - min_number

    print("#{} {}".format(tc, result))


