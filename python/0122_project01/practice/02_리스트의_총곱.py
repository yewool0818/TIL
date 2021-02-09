'''
리스트의 총곱

사용자가 입력한 정수 num을 기준으로, 1~num으로 이루어진 리스트의 총 곱을 구하는 함수를

1. `for`문을 사용하여
2. `while`문을 사용하여

작성하시오.
'''

# for문만 사용하여 풀기
def mul_with_for(numbers):
    # 1. 변수 초기화
    total = 1

    # 2. numbers 순회(반복)
    for number in numbers:
        # 3. 해당 수 변수에 곱해주기
        total *= number

    # 4. 총 곱 반환
    return total


# while문만 사용하여 풀기
def mul_with_while(numbers):
    # 1. 변수 초기화
    total = 1  # 총 곱
    i = 0      # 리스트 인덱스

    # 2. numbers의 각 요소 순회(반복) - 리스트길이가 인덱스+1보다 크거나 같을 때까지
    while len(numbers) >= i+1 :
        # 3. total에 number의 i번째 인덱스 곱하기
        total *= numbers[i]
        # 4. i = index값 1씩 증가
        i += 1
    
    # 5. 총 곱 반환
    return total


# 아래 코드는 바꾸지 않습니다.
if __name__ == '__main__':
    num = int(input('정수를 입력하세요'))
    numbers = list(range(1, num+1))

    # 아래 두코드 모두 in 4 => out 24 / in 5 => out 120 를 만족해야 합니다.
    print(mul_with_for(numbers))
    print(mul_with_while(numbers))