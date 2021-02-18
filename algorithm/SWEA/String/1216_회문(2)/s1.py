import sys

sys.stdin = open("input.txt")

def palindrome(word, length):
    # 팰린드롬 단어의 개수
    count = 0

    # 단어의 길이를 절반만큼 인덱스 순회하며, 회문 여부 확인
    # 단어의 양 끝부터 중간부분까지 탐색
    for i in range(length//2):
        # 주어진 단어의 앞, 뒤값이 서로 동일하다면 count에 1추가
        if word[i] == word[length-i-1]:
            count += 1
            # count가 주어진 단어의 길이의 반과 동일하다면
            if count == length //2:
                # 해당 단어가 팰린드롬이다.
                # 그 단어의 개수를 출력하자
                count = len(word)
        # 표면->중간으로 탐색을 하다가 서로 다르면 count를 0으로 바꿔주고
        # 탐색 종료
        else:
            count = 0
            break

    return count


T = 10

for tc in range(1, T + 1):
    testCase = int(input())
    # board : 100X100 글자판
    board = [[char for char in input()] for _ in range(100)]
    # 전치행렬
    new_board = list(zip(*board))

    # 출력값 초기화 : 회문 길이
    result = 0
    result1 = 0
    result2 = 0

    # 행 우선 탐색
    # 각 행에 회문의 길이가 99개인게 있는지 -> 97개 인게 있는지 -> 있다면 stop
    # result에 길이 할당
    for length in range(100, 0, -1):
        for row in range(100):
            for col in range(100-length+1):
                word = board[row][col:col+length]
                col_word = new_board[row][col:col+length]
                if palindrome(word, length) or palindrome(col_word, length):
                    result1 = palindrome(word, length)
                    result2 = palindrome(col_word, length)
                    if result1 > result2:
                        result = result1
                    else:
                        result = result2
                    break
            if result1 or result2: # result에 값이 할당되었으면 빠져나오기
               break
        if result1 or result2:
            break



    print("#{} {}".format(testCase, result))
