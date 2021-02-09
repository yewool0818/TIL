import sys
sys.stdin = open("input.txt")

T = 10

def check_view(n, buildings):
    # 각 건물들의 앞, 앞앞 건물 층수를 뺀것과 뒤, 뒤뒤 건물의 층수를 뺀 것이
    # 양수이면 ok - 각 4개의 값 중 가장 작은 값을 get

    # 결과값 초기화
    view = 0

    # 맨 앞과 끝 2개는 강이므로 건물 조회에서 제외한다.
    for i in range(2, n-2):
        # 현재 건물의 층 수 에서 앞 건물 빼기
        a = buildings[i] - buildings[i-2]
        b = buildings[i] - buildings[i-1]
        c = buildings[i] - buildings[i+1]
        d = buildings[i] - buildings[i+2]
        diffs = [a, b, c, d]

        # 4가지 경우 모두가 양수인지 확인
        if a > 0 and b > 0 and c > 0 and d > 0:
            # 모두 양수라면 그 중에서 가장 작은 값을 view에 더해주기
            view += min(diffs)

    return view

for tc in range(1, T+1):
    n = int(input())
    buildings = list(map(int, input().split()))
    result = check_view(n, buildings)
    print("#{} {}".format(tc, result))


