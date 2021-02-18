import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):

    # P : 전체 페이지의 수
    # Pa, Pb : 각 A, B가 찾을 쪽 번호
    P, Pa, Pb = map(int, input().split())

    # 탐색 !
    # A, B : 각 A, B가 탐색한 횟수
    A = 0
    B = 0

    # 이진탐색
    Al = 1 # 첫 페이지
    Ar = P # 마지막 페이지
    Ac = 0 # 현재 페이지

    while True:
        A += 1

        # 가운데를 펼쳐보자 - 현재 페이지
        Ac = (Al+Ar) // 2

        # 찾으려는 페이지와 현재 페이지를 비교해보자
        if Ac > Pa: # 현재 페이지가 찾으려는 페이지보다 크다면 - 왼쪽 보기
            Ar = Ac # 오른쪽의 기준을 현재 페이지로
        elif Ac < Pa: # 현재 페이지가 찾으려는 페이지보다 작다면 - 오른쪽 보기
            Al = Ac # 왼쪽의 기준을 현재 페이지로!
        else: # 현재 페이지가 찾으려는 페이지와 일치하면 - 끝!
            break

    # B의 이진탐색
    Bl = 1
    Br = P
    Bc = 0

    while True:
        B += 1

        # 가운데를 펼쳐보자 - 현재 페이지
        Bc = (Bl+Br) // 2

        # 찾으려는 페이지와 현재 페이지를 비교해보자
        if Bc > Pb: # 현재 페이지가 찾으려는 페이지보다 크다면 - 왼쪽 보기
            Br = Bc # 오른쪽의 기준을 현재 페이지로
        elif Bc < Pb: # 현재 페이지가 찾으려는 페이지보다 작다면 - 오른쪽 보기
            Bl = Bc # 왼쪽의 기준을 현재 페이지로!
        else: # 현재 페이지가 찾으려는 페이지와 일치하면 - 끝!
            break


    # 출력값 : 이진탐색을 통해 더 빨리 페이지를 찾은 사람 (비기면 0)
    if A > B :
        result = 'B'
    elif A < B:
        result = 'A'
    else:
        result = 0

    print("#{} {}".format(tc, result))
