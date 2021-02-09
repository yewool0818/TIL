'''
N 까지의 총합

정수 num을 기준으로, 1~num까지의 총 합을 구하는 함수를

1. `for` 문을 사용하여
2. `while`문을 사용하여

작성하시오.
'''
a = 3
print(a)


# for문만 사용하여 풀기
def sum_with_for(num):
    # 1. 변수 초기화
    total = 0

    # 2. 1부터 num까지 순회
    for i in range(1, num+1):
        # 3. total에 해당 숫자 더해주기
        total += i

    # 4. 총합 반환
    return total


# while문만 사용하여 풀기
def sum_with_while(num):
    # 1. 변수 초기화
    total = 0 # 총 합

    # 2. 1부터 num까지 더하기 반복 (num이 0이 될 때까지)
    while num > 0:
        # 3. 해당 숫자 더하기
        total += num
        # 4. 해당 숫자에서 1씩 빼주기
        num -=1

    # 5. 총 합 반환
    return total

# 아래 코드는 바꾸지 않습니다.
if __name__ == '__main__':
    print(sum_with_for(4))    # 10
    print(sum_with_while(4))  # 10
    print(sum_with_for(5))    # 15
    print(sum_with_while(5))  # 15

