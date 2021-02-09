import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
    temp_list = [0]*12

    # 들어오는 값
    numbers = input()

    for number in numbers:
        temp_list[int(number)] += 1 # num의 맨 마지막 값이 temp_list의 num번째 인덱스에 1 추가된다.

    i = 0
    tri = 0
    runn = 0

    while i < 10:
        # triplete 조사 후 데이터 삭제
        if temp_list[i] >= 3:
            temp_list[i] -= 3
            tri += 1
            continue # 이 조건 충족 시, 밑에 실행하지 말고 while문 한번 다시 동장

        # run 조사 후 데이터 삭제
        if temp_list[i] >= 1 and temp_list[i+1] >= 1 and temp_list[i+2] >=1 :
            temp_list[i] -=1
            temp_list[i+1] -=1
            temp_list[i+2] -=1
            runn += 1
            continue

        i += 1

    if runn + tri == 2:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))