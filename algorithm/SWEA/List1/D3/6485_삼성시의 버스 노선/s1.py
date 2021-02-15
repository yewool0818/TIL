import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N : 버스의 수
    N = int(input())

    # 버스 정류장 리스트 생성 (1~5000번)
    bus_stop = [0 for _ in range(5001)]

    for i in range(N):
        # A, B : 각 i번쨰 노선의 버스 번호(A이상 B이하)
        A, B = map(int, input().split())

        # 해당 정류장에 지나는 버스의 대수 누적
        for j in range(A, B+1):
            bus_stop[j] += 1


    # P : 우리가 확인하고 싶은 버스 정류장의 수
    P = int(input())

    print("#{}".format(tc), end=" ")
    
    for i in range(P):
        # C : 우리가 확인하고 싶은 정류장의 번호
        C = int(input())
        print(bus_stop[C], end=" ")

    print()