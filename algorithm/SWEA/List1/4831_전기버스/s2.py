import sys
sys.stdin = open("input.txt")


T = int(input())

def elect_bus(K, N, M, stations):

    # 충전소의 위치를 1로 표기
    chargable_stations = [0 for _ in range(N)]

    for i in range(N):
        if i in stations:
            chargable_stations[i] = 1

    # 충전 횟수
    result = 0
    # 남은 에너지
    energy = K
    # 이동한 거리 == 현재 위치
    move = 0

    # 이동한 거리가 종점보다 커지기 전까지 반복
    while move < N-1:
        # 한 정거장 이동 시, 에너지 -1, 이동 거리 +1
        energy -= 1
        move += 1
        
        # 충전소가 있을 때
        if chargable_stations[move] == 1:
            # 다음에 올 정류장들을 살펴보고
            for j in range(move+1, N):
                # 다음 충전소가 있으면,
                if chargable_stations[j] == 1:
                    # 다음 충전소 거리보다 현재 에너지가 적으면 충전
                    if energy < j - move: # j : 다음 충전소의 위치
                        # 에너지를 다시 K 만큼 충전
                        energy = K
                        # 충전 횟수 1 증가
                        result += 1
                    break # 충전소에서 충전했으면 나가라

                # 다음 충전소가 없을 경우,
                # 최종 목적지까지 거리보다 에너지가 적으면 충전
                if j == N-1:
                    energy = K
                    result += 1

        # 최종 목적지 전에 전기가 바닥나면 종료
        if energy == 0:
            return 0

    return result


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