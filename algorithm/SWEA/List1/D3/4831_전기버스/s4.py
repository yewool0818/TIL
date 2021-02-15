import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 1. 입력 변수
    #    K : 한번의 충전으로 나아갈 수 있는 정류장 수
    #    N : 종점 정류장 번호
    #    M : 총 충전 정류장의 개수
    K, N, M = map(int, input().split())

    # 충전소 정류장 리스트
    charge = list(map(int, input().split()))
    ans = 0  # 충전 횟수
    
    # 아래와 같은 코드 - 출발지 + 충전소들 + 도착지
    charge = [0] + charge + [N]
    # charge.insert(0, 0)  # 0번째에 0을 추가
    # charge.append(N)     # 마지막에 N을 추가

    # 마지막 버스의 위치 (현재 위치)
    last = 0

    # 2. 앞으로 가면서 충전소를 만났을 때,
    #    현재 위치와 다음 충전소의 위치의 차이와 나의 에너지를 비교해서
    #    -> 에너지가 더 크다 -> 갈 수 있다
    #    -> 에너지가 부족하다 -> 갈 수 없다

    for i in range(1, M+2): # 입력받은 충전소의 개수보다 2칸을 늘렸으니 M+2까지!
        if charge[i] - charge[i-1] > K:
            ans = 0
            break

        # 갈 수 없다면 아무 작업 X
        # 갈 수 없다면 내 바로 직전 충전소로 위치를 옮기고 횟수 1회 증가
        if charge[i] > last + K:
            last = charge[i-1]
            ans += 1
            break


    print("#{} {}".format(tc, ans))