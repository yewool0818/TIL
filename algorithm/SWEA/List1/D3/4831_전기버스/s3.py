import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 1. 입력 변수
    #    K : 한번의 충전으로 나아갈 수 있는 정류장 수
    #    N : 종점 정류장 번호
    #    M : 총 충전 정류장의 개수
    K, N, M = map(int, input().split())

    # 충전소 정류장 리스트
    charge = list(map(int, input().split()))

    # 버스 정류장 리스트를 만들어 충전소를 표시하자!
    bus_stops = [0 for _ in range(N)]

    # for i in charge:
    #     bus_stops[i] = 1

    for i in range(M):
        bus_stops[charge[i]] = 1

    bus = 0 # 버스 위치
    ans = 0 # 충전 횟수

    # 2. 일단 갈 수 있는 만큼 앞으로 쭉 가보고,
    #    에너지가 다 떨어지면 뒤로 다시 뒤돌아 가서 충전소를 확인하고 충전하자
    while True:
        # 버스가 이동할 수 있는 만큼 이동을 하자
        bus += K

        # 종점에 도착하거나 종점을 지나 더 나아간 경우 종료하겠다!
        if bus >= N: break

        for i in range(bus, bus-K, -1):
            # 되돌려 가는 동안(내 원래 충발자리 전에) 버스 충전소가 있다면
            # if bus_stops[i] == 1:
            if bus_stops[i]:
                ans += 1
                bus = i # 버스 위치를 충전소 위치로 되돌려 놓기
                break   # 충전했으면 반복 중지 - else 실행

        # 3. 만약 원래 있던 위치까지 가는 동안 충전소가 없다면 나는 종점까지 갈 수 없는 것이다.
        else:
            ans = 0
            break

    print("#{} {}".format(tc, ans))





