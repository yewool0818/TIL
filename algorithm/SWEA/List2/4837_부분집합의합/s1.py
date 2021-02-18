import sys

sys.stdin = open("input.txt")

T = int(input())

# A : 1부터 12까지의 숫자를 원소로 가진 집합
A = [int(i) for i in range(1, 13)]

for tc in range(1, T + 1):
    # N : 부분집합 원소의 수
    # K : 부분집합의 합
    N, K = map(int, input().split())

    # 원소의 합이 K인 부분집합의 개수
    result = 0

    # 부분집합을 넣을 빈 리스트
    subsets = []

    # 부분집합 구하는 과정
    # 1. 모든 부분집합 개수만큼 반복
    for i in range(1<<12):
        # 각 부분 집합
        subset = []

        # 2. 모든 원소의 개수만큼 반복
        # : j를 부분집합의 각 원소에 접근하는 인덱스로 활용
        for j in range(12):

            # 3. 해당 인덱스에 부분집합의 요소가 포함되어있는지 확인
            if i & (1<<j):
                # 부분집합 리스트를 생성
                subset.append(A[j])

        # 부분집합의 길이가 N개 인것만 subsets에 포함
        if len(subset) == N:
            subsets.append(subset)


    # subsets 중 total이 K인것일 때 result에 1씩 추가
    for subset in subsets:
        # 한 부분집합에 대한 각 요소의 합
        total = 0
        for element in subset:
            total += element
        if total == K:
            result += 1


    print("#{} {}".format(tc, result))