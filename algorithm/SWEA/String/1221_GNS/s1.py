import sys

sys.stdin = open("input.txt")

T = int(input())

chars = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T + 1):
    # 테스트 케이스 및 문자열 개수 입력받기 - a는 안쓸꺼라 변수명 대충 지음
    a, N = input().split()
    N = int(N) # 근데 N도 결국 안씀

    # 문자열 입력받기
    input_chars = list(input().split())

    # 정렬된 문자열을 담을 빈 리스트
    sorted_chars = []

    # chars 반복
    for i in range(len(chars)):
        for ichar in input_chars:
            if ichar == chars[i]:
                sorted_chars.append(ichar)

    print("#{} {}".format(tc, ' '.join(sorted_chars)))