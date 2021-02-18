import sys

sys.stdin = open("input.txt")

def compare_str(str1, str2):
    # str2에 str1과 일치하는 부분이 있으면 1 출력, 아니면 0 출력
    # : 항상 str2가 str1보다 더 길다!

    # 결과 출력할 변수 초기화
    result = 0

    # N : str1의 길이
    # M : str2의 길이
    N, M = len(str1), len(str2)

    # 풀이 계획:
    # str1의 위치를 한칸씩 오른쪽으로 움직이며,
    # str2에 맞춰가며 str1이 str2에 완전히 일치하는 순간이 있으면
    # result=1을 출력한다.

    for i in range(M-N+1):
        # str1을 str2의 0번째 인덱스부터 M번째 인덱스까지 맞춰간다는 느낌으로 비교
        if str2[i:i+N] == str1:
            result = 1
            break


    return result


T = int(input())

for tc in range(1, T + 1):
    # str1 : 첫 번째 문자열
    # str2 : 두 번째 문자열
    str1 = input()
    str2 = input()
    result = compare_str(str1, str2)

    print("#{} {}".format(tc, result))