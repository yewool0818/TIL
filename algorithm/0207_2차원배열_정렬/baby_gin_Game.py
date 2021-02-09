import random

# 3장 연속 : run
# 3장 동일한 번호 : triplet
# 6장 전체가 nun & triplet or 2run or 2triple => baby-gin

numbers = 667767

def baby_gin(numbers):
    sorted_numbers = sorted([int(number) for number in numbers])
    number_group_1 = sorted_numbers[:3]
    number_group_2 = sorted_numbers[3:]

    # triplet 확인
    if number_group_1[0] == number_group_1[1] and number_group_1[1] == number_group_1[2]:
        if number_group_2[0] == number_group_2[1] and number_group_2[1] == number_group_2[2]:
            return True;
        elif number_group_2[0]+1 == number_group_2[1] and number_group_2[1]+1 == number_group_2[2]:
            return True;
        else:
            return False;

    # run 확인    
    elif number_group_1[0]+1 == number_group_1[1] and number_group_1[1]+1 == number_group_1[2]:
        if number_group_2[0] == number_group_2[1] and number_group_2[1] == number_group_2[2]:
            return True;
        elif number_group_2[0]+1 == number_group_2[1] and number_group_2[1]+1 == number_group_2[2]:
            return True;
        else:
            return False;

    else:
        return False;



print(baby_gin('235777'))
# 위 식의 경우 [1, 2, 3, 1, 2, 3]을 정렬하면 [1, 1, 2, 2, 3, 3]으로 정렬되어 실패할 수 있다.



# Solution

num = 123123

# 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
c = [0] * 12

for _ in range(6):
    c[num % 10] += 1 # num의 마지막 값이 c의 num번째 인덱스에 1이 추가된다.
    num //= 10 # num의 맨 마지막 값을 지운다.

# c = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
# 리스트 c에  4,5,6,7,8,9번재 인덱스가 각 1씩 추가되어있다.
print(c)

i = 0 
tri = run = 0

while i < 10:
    if c[i] >= 3: # triplete 조사 후 데이터 삭제 - triple일 경우 3이상이 한 인덱스 값에 누적되어있을 것이다.
        c[i] -= 3 # tri에 1 더해줘야하니까 3을 빼준다.
        tri += 1
        continue; # 이 조건 충족 시 멈추지 말고 다음 조건 실행!

    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run w조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue;
    
    i+= 1

if run + tri == 2 : print("Baby Gin")
else: print("Lose")