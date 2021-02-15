import sys
sys.stdin = open("input.txt")


T = int(input())

def elect_bus(K, N, M, stations):

    # 버스의 현재 위치
    bus_loc = 0
    # 충전 횟수
    count = 0

    # 현재 위치에서 K(갈수있는 정류장 수)를 더하더라도
    # N(종점)보다 작으면 간다.
    while bus_loc + K < N:
        # 최소한으로 하기 위해 K, K-1, K-2, .., 1 순으로 움직였을 때 충전소 있는지 확인
        for move in range(K, 0, -1):
            # 가는 길에 충전소가 있다면!
            if bus_loc + move in stations:
                # 현재 위치에서 move만큼 이동해
                bus_loc += move
                # 충전 횟수 증가
                count += 1
                # 반복 끝
                break

        # 충전소가 없다면 앞으로 못간다.
        else:
            return 0

    return count


for tc in range(1, T + 1):

    # K : 한 번 충전으로 이동할 수 있는 정류장 수
    # N : 종점 정류장 번호
    # M : 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())
    # 충전기 설치 정류장 번호 리스트
    stations = [int(i) for i in input().split()]
    # 충전소 몇번 들리는지 체크
    result = elect_bus(K, N, M, stations)

    print('#{} {}'.format(tc, result))