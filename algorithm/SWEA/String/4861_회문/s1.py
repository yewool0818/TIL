import sys

sys.stdin = open("input.txt")

T = int(input())

def palindrome(word, M):
    pal_word = ''
    count = 0

    # 회문의 길이의 절반만큼 인덱스 순회하며 회문 여부 확인
    for i in range(M // 2):
        # 주어진 단어의 앞, 뒤값이 서로 동일하다면 count에 1추가
        if word[i] == word[M-i-1]:
            count += 1
            # count가 주어진 단어의 길이의 반과 동일하다면
            if count == M//2:
                # 해당 단어가 팰린드롬이다.
                pal_word = ''.join(word)
        else:
            count = 0

    return pal_word



for tc in range(1, T + 1):
    # N : 글자판의 크기
    # M : 회문의 길이
    N, M = map(int, input().split())

    # board : 글자판
    board = [[char for char in input()] for _ in range(N)]
    # board 출력 예시
    #  [['G', 'O', 'F', 'F', 'A', 'K', 'W', 'F', 'S', 'M'],
    #   ['O', 'Y', 'E', 'C', 'R', 'S', 'L', 'D', 'L', 'Q'],
    #   .. ]]
    
    # 결과값으로 출력할 회문 초기화
    result = ''


    # 행 방향에 있는지 확인
    for row in range(N):
        # M개 길이만큼 잘라서 회문인지 확인
        for i in range(N-M+1):
            word = board[row][i:i+M]
            # 회문의 결과값이 나오면 result에 할당
            if palindrome(word, M):
                result = palindrome(word, M)


    # 열 방향에 있는지 확인
    for row in range(N):
        temp_words = []
        for col in range(N):
            temp_word = board[col][row]
            temp_words.append(temp_word)
            for i in range(N-M+1):
                word = temp_words[i:i+M]
        if palindrome(word, M):
            result = palindrome(word, M)

    print("#{} {}".format(tc, result))

