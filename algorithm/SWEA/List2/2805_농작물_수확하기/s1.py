import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N : 농장의 크기
    N = int(input())

    # farm : 농장의 가치를 담은 2차원 리스트
    farm = [[int(val) for val in input()] for _ in range(N)]

    # 가치를 모두 더한 결과값 초기화
    result = 0

    # 시작 - 가운데
    # 반복 - 가운데 + 양옆1칸씩
    # 변화의 시작 - 더하는 영역이 N이랑 똑같아지면
    # 반복 - 지금까지의 영역 - 양옆1칸씩
    # 끝 - 반복이 N번되면

    # 가운데 인덱스
    c_idx = N // 2

    # 행
    row = 0

    # 확장될 때는 N을 2로 나눈 몫만큼 확장된다.
    for i in range(N//2 + 1):
        # 중앙 인덱스에서 순차적으로 앞뒤 인덱스를 늘리며 더해준다
        result += sum(farm[row][c_idx-i:c_idx+i+1])
        row += 1

    # 이제 줄어든다
    # 줄어들 때는 N//2(맨 가운데 행)은 더했으니, 그 다음부터 진행해야 해서 하나 빼고
    # 거꾸로 1씩 진행되도록 진행한다.
    for j in range(N//2 - 1, -1, -1):
        # 중앙 인덱스에서 순차적으로 앞뒤 인덱스를 줄이며 더해준다
        result += sum(farm[row][c_idx-j:c_idx+j+1])
        row += 1


    print("#{} {}".format(tc, result))
