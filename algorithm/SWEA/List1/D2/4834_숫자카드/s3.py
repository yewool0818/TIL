import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # N : 카드 장수
    N = int(input())
    # 카드 리스트
    cards = [int(card) for card in input()]

    # 1. 카드 번호 개수만큼 0으로 된 리스트를 만든다.
    # counts 배열 생성
    counts = [0 for _ in range(10)] # 카드 숫자가 0부터 9까지 될 수 있으므로

    max_num = 0    # 가장 많은 카드의 번호
    max_count = 0  # 가장 많은 카드의 장수

    # 2. 카드 번호가 각 리스트 번호에 들어올 때 마다 1씩 증가한다.(count 증가)
    # 3. 가장 숫자가 높은 리스트의 인덱스를 뽑는다.
    #    - 이 때 두개 이상일 경우 인덱스값이 높은 것을 뽑는다.


    # 방법 1
    # for i in cards:
    #     counts[i] += 1

    # for i in range(len(counts)):
    #     # 이곳에 등호가 들어간 이유를 잘 생각해보자.. - 중복되면 더 큰 수로 대체해야해서!
    #     if max_count <= counts[i]:
    #         max_num = i
    #         max_count = counts[i]


    # 방법 2
    for i in cards:
        # counts 배열 생성
        counts[i] += 1
        # 여기서 바로 max_count 값 뽑기
        if max_count < counts[i]:
            max_count = counts[i]

    # counts 배열에서 거꾸로 보기
    # - why? num이 큰 값부터 보면 가장 큰 수를 만났을 때 바로 break해주면 되니까!
    # range(len(counts) - 1, -1, -1) :  counts의 맨 끝 인덱스부터 0(처음) 인덱스까지 앞으로 한칸씩 가자
    for i in range(len(counts) - 1, -1, -1):
        if max_count == counts[i]:
            max_num = i
            break

    print("#{} {} {}".format(tc, max_num, max_count))
